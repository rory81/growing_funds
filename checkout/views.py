from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import Order
from .forms import OrderForm
from projects.models import Project

import stripe

def checkout(request, pk=None):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        total = int(order_form['amount_pledged'].value())
        stripe_total = round(total * 100)
        stripe.api_key =stripe_secret_key
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
    # if request.method == 'POST':
    #     redirect()
    #     order_form = OrderForm(request.POST)
    #     if order_form.is_valid():
    #         order = order_form.save(commit=False)
    #         project.raised += order.amount_pledged
    #         stripe_total = round(order.amount_pledged * 100)
    #         order.save()
    #         project.save()
            
    #         stripe.api_key =stripe_secret_key
    #         stripe.PaymentIntent.create(
    #             amount=stripe_total,
    #             currency=settings.STRIPE_CURRENCY,
    #         )
    # else:
    
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'project':project,
        'stripe_public_key':stripe_public_key,
        'client_secret':intent.client_secret
    }

    return render(request, 'checkout.html', context)

