from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .forms import OrderForm
from projects.models import Project
from .models import Order
import json


import stripe

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY
stripe.api_key = stripe_secret_key


def checkout(request, pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None
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
        total = int(request.POST['amount_pledged'])
        # print('Data:', request.POST)
        customer = stripe.Customer.create(
            source=request.POST['stripeToken']
        )
        intent = stripe.PaymentIntent.create(
            amount=total*100,
            currency="usd",
            payment_method_types=["card"],
            customer=customer,
        )

        stripe.PaymentIntent.confirm(
            intent.id,
            payment_method="pm_card_visa",
        )

        # charge = stripe.Charge.create(
        #     customer=customer,
        #     amount=total*100,
        #     currency=settings.STRIPE_CURRENCY
        # )
        if order_form.is_valid:
            print(intent.status)
            order = order_form.save()
            order.project = Project.objects.get(pk=pk)
            order.save(update_fields=["project"])
            request.session['save_info'] = 'save-info' in request.POST
        else:
            messages.error(request, 'There was an error with your form. \
            Please double check your information.')

    else:
        order_form = OrderForm()

    context = {
        'project': project,
        'client_secret': intent.client_secret,
    }
    return redirect(reverse('success', args=[total]))


# def success(request, total, pk, order_number):
#     amount = total
#     save_info = request.session.get('save_info')
#     order = get_object_or_404(Order, order_number=order_number)
#     print(order.order_number)
#     project = get_object_or_404(Project, pk=pk)
#     project.raised += amount
#     project.save(update_fields=["raised"])

    # return render(request, 'payment_success.html', context)