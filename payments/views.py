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
            fund.raised += fund.donation
            fund.project = Project.objects.get(pk=pk)
            fund.date = datetime.now()
            fund.save()
 
    else:
        payment_form =MakePaymentForm()
        fund_form=FundForm()
    return render(request, "payment.html",{'project':project,'fund_form':fund_form, 'payment_form': payment_form, 'publishable':settings.STRIPE_PUBLISHABLE})

