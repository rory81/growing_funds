from django.utils import timezone
from datetime import datetime
from .models import Project, Category
from .views import calculations
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect



def categories(request):
    """
    show the categories on all templates dynamically
    """
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return context

def searchbar(request):

    projects = Project.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date')
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(searchbar)
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            projects = projects.filter(queries)
    
    calculations(projects)

    context = {
        'projects': projects,
        'search_term':query,
    }

    return render(request, 'projects.html', context)



