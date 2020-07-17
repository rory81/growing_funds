from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Order
from .forms import Orderform
from projects.models import Project

def checkout(request, pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None
    if project.num_days <= 0:
        messages.error(request, "This Project has ended")
        return redirect(reverse('projects'))
    
    order_form = Orderform()

    context = {
        'order_form': order_form,
        'project':project,
        'stripe_public_key':'pk_test_cNaEktD3FLhzwdSNbRXkXVTj00G0gYDSd9',
        'client_secret':'sk_test_BtwZhL1UIpDD2PNYzAkVzPRD00T3zWDRpV'
    }

    return render(request, 'checkout.html', context)
