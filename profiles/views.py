from django.shortcuts import render


def profile(request):
    context = {}

    return render(request, 'profile.html', context)
