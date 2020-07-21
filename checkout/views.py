from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
import json
from .models import Order
from .forms import OrderForm
from projects.models import Project

import stripe

def success(request):
    return render(request, 'payment_success.html')

def cancel(request):
    return render(request, 'payment_success.html')

def create_session(request, pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == 'POST':
        data = json.loads(request.data)
        session = stripe.checkout.Session.create(
            success_url='http://localhost:127.0.0.1/success?id={CHECKOUT_SESSION_ID}',
            cancel_url='http://localhost:127.0.0.1/cancel',
            submit_type='donate',
            payment_method_types=['card'],
            line_items=[{
            'amount': data['amount'],
            'name': 'Pledge',
            'billing_address_collection': required,
            'currency': 'USD',
            'quantity': 1
            }],
            metadata={
            'cause': data['cause'],
            }
        )
        return jsonify(session)
    return render(request, 'checkout.html', {'project':project})

def get_session(request):
    session = stripe.checkout.Session.retrieve(
        request.args['id'],
        expand=['payment-intent'],
    )
    return jsonify(session)