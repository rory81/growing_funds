from django.shortcuts import render
from .models import Project
from datetime import datetime
from django.utils import timezone

def get_percentage_raised():

    projects = Project.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    for project in projects:
        project.percentage= round(((project.raised/project.goal)*100),1)

    return {'projects':projects}

