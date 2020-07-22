from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .models import Order
from .forms import OrderForm
from projects.models import Project


import stripe

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY
stripe.api_key =stripe_secret_key

def checkout(request, pk=None): 
    project = get_object_or_404(Project, pk=pk) if pk else None
    order_form = OrderForm()

    context = {
        'project':project,
        'order_form': order_form,
        'stripe_public_key':stripe_public_key,
    }

    return render(request, 'checkout.html', context)


def charge(request, pk=None):  
    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == 'POST':
        total= int(request.POST['amount_pledged'])
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


#  1. Seperate where you choose how much you donate within a form, 
#  2. post that form to new function which only renders the checkout, and creates the intent.  
#  3. then have your function which takes a post to actually handle whatever you want to happen once the payment has gone through