from django.utils import timezone
from datetime import datetime
from .models import Project, Category
from django.conf import settings


def categories(request):
    """
    show the categories on all templates dynamically
    """
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return context


def calculations(request):
    """
    calculate the num_days and percentage_raised for every template
    """
    projects = Project.objects.all()

    for project in projects:
        project.percentage = round(((project.raised/project.goal)*100), 1)
        project.num_days = (project.end_date - datetime.now().date()).days

    context = {
        'percentage': project.percentage,
        'num_days': project.num_days
    }

    return context