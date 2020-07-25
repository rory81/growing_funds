from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from .forms import OrderForm
from projects.models import Project


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
        total = int(request.POST['amount_pledged'])
        print('Data:', request.POST)
        customer = stripe.Customer.create(
            source=request.POST['stripeToken']
        )
        # intent = stripe.PaymentIntent.create(
        #     amount=total,
        #     currency=settings.STRIPE_CURRENCY,
        #     payment_method_types=['card'],
        #     customer=customer,
        # )
        charge = stripe.Charge.create(
            customer=customer,
            amount=total*100,
            currency=settings.STRIPE_CURRENCY
        )

    return redirect(reverse('success', args=[total]))


def success(request, args):
    amount = args
    return render(request, 'payment_success.html', {'amount': amount})
