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


