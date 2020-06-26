from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from .models import Project, Category
from .forms import StartProjectForm
# from django import template
# from django.core.paginator import Paginator


def get_projects(request):
    """
    Create a view that will return a list op Projects
    that were created prior to 'now'
    and render them to the 'projects.html' template
    """
    projects = Project.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date')
    for project in projects:
        project.percentage = round(((project.raised/project.goal)*100), 1)
        project.num_days = (project.end_date - datetime.now().date()).days
    return render(request, 'projects.html', {'projects': projects})


def get_project_category(request, project_category):
    """
   per category

    """
    projects = Project.objects.filter(
        category=Category.objects.get(category=project_category).id).order_by('-created_date')
    projects.category = project_category
    for project in projects:
        project.percentage = round(((project.raised/project.goal)*100), 1)
        project.num_days = (project.end_date - datetime.now().date()).days

    return render(request, 'project_category.html', {'projects': projects})

    return render(request, 'project_category.html')


def project_detail(request, pk):
    """
    Create a view that returns a single project object
    based on the project_ID (pk)
    and render it to the 'projectdetail.html' template
    or return a 404 error if the post is not found.
    """
    project = get_object_or_404(Project, pk=pk)
    project.views += 1
    project.num_days = (abs(datetime.now().date() - project.end_date)).days
    project.save()
    return render(request, 'projectdetail.html', {'project': project})


def create_or_edit_project(request, pk=None):
    """
    Create a view that allows to create or edit a project,
    depending if the Project_id is null or not
    """
    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == "POST":
        form = StartProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect(project_detail, project.pk)
    else:
        form = StartProjectForm(instance=project)
    return render(request, 'startprojectform.html', {'form': form})
