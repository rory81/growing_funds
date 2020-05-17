from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import stripe
from .forms import MakePaymentForm, FundForm
from .models import Fund
from projects.models import Project
from datetime import datetime

stripe.api_key = settings.STRIPE_SECRET

"""
@login_required()
remove quotes when the login and auth app has been realized
"""
def funding(request,pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method=="POST":
        fund_form = FundForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if fund_form.is_valid() and payment_form.is_valid():
            fund = fund_form.save(commit=False)
            fund.date = datetime.now()
            fund.project = Project.title
            fund.raised += fund.amount
            fund.save()
            
            
            try: 
                customer = stripe.Charge.create(
                    amount = int(request.amount *100),
                    currency = "USD",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'], 
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                return redirect(reverse('projects'))
            
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form =MakePaymentForm()
        fund_form=FundForm()
    return render(request, "payment.html",{'project_title':project.title,'fund_form':fund_form, 'payment_form': payment_form, 'publishable':settings.STRIPE_PUBLISHABLE})

