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
    }

    return render(request, 'checkout.html', context)
