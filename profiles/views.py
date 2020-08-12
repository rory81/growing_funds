from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from projects.models import Project
from projects.views import calculations
from checkout.models import Order
from .forms import UserProfileForm
from django.contrib import messages


def profile(request):
    """
    creating a profile form to enter or update user information
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    projects = profile.projects.all()
    calculations(projects)
    context = {
        'form': form,
        'orders': orders,
        'projects': projects,
    }

    return render(request, 'profile.html', context)
