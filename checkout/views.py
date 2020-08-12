from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .forms import OrderForm
from projects.models import Project
from .models import Order
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY
stripe.api_key = stripe_secret_key


def checkout(request, pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,

            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()
    context = {
        'project': project,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
    }

    return render(request, 'checkout.html', context)


def charge(request, pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        # PAYMENT
        total = str(float(request.POST['amount_pledged']))
        stripe_total = float(request.POST['amount_pledged'])*100
        # print('Data:', request.POST)
        print("stripe_total", stripe_total)
        customer = stripe.Customer.create(
            source=request.POST['stripeToken']
        )
        intent = stripe.PaymentIntent.create(
            amount=int(stripe_total),
            currency="usd",
            payment_method_types=["card"],
            customer=customer,
        )

        confirm = stripe.PaymentIntent.confirm(
            intent.id,
            payment_method="pm_card_visa",
        )

        if order_form.is_valid and confirm.status == 'succeeded':
            order = order_form.save()
            order.project = Project.objects.get(pk=pk)
            order.save(update_fields=["project"])
            request.session['save_info'] = 'save-info' in request.POST
        else:
            messages.error(request, 'There was an error with your form or creditcard. \
            Please double check your information.')

    else:
        order_form = OrderForm()


    return redirect(reverse('success', args=(total, pk, order.order_number)))


def success(request, total, pk, order_number):
    amount = float(total)
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    project = get_object_or_404(Project, pk=pk)
    project.raised += amount
    project.save(update_fields=["raised"])

    new_line ='\n'
    send_mail(
        f'Growing Funds: confirmation order {order_number}',
        f'Dear {profile.user},{new_line}{new_line}Thank you for pledging ${amount} to project {project.title}{new_line}Hope to see you again soon.{new_line}{new_line}Kind Regards, Growing Funds ',
        'GrowingFunds <settings.EMAIL_HOST_USER>',
        [request.user.email],
        fail_silently=False,
    )

    context = {
        'project': project,
        'amount': amount,
        'order': order,
    }
    return render(request, 'payment_success.html', context)
