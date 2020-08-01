from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from .models import Project, Category
from .forms import StartProjectForm
from profiles.models import UserProfile


def calculations(projects):
    """
    calculate the num_days and percentage_raised for every template
    """

    for p in projects:
        p.percentage = round(((p.raised/p.goal)*100), 1)
        p.num_days = (p.end_date - datetime.now().date()).days
    return projects


def get_projects(request):
    """
    Create a view that will return a list op Projects
    that were created prior to 'now'
    and render them to the 'projects.html' template
    """
    projects = Project.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('get_projects'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            projects = projects.filter(queries)
            results = projects.filter(queries)

    calculations(projects)

    context = {
        'projects': projects,
        'search_term': query,
    }

    return render(request, 'projects.html', context)


def get_project_category(request, project_category):
    """
    Projects for a specific category

    """
    projects = Project.objects.filter(
        category=Category.objects.get(category=project_category).id).order_by('-created_date')
    projects.category = project_category

    calculations(projects)

    context = {
        'projects': projects,

    }

    return render(request, 'project_category.html', context)


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

    context = {
        'project': project,
    }
    return render(request, 'projectdetail.html', context)


def create_or_edit_project(request, pk=None):
    """
    Create a view that allows to create or edit a project,
    depending if the Project_id is null or not
    """
    project = get_object_or_404(Project, pk=pk) if pk else None

    if request.method == "POST":
        form = StartProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            profile = UserProfile.objects.get(user=request.user)
            project.user_profile = profile
            project = form.save()
            return redirect(project_detail, project.pk)
    else:
        form = StartProjectForm(instance=project)

    context = {
        'form': form,
    }
    return render(request, 'startprojectform.html', context)


def delete_project(request, pk):
    """
    Create a view that allows to delete a project,
    """
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('profile')
