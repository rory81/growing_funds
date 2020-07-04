from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
from .models import Project, Category
from .forms import StartProjectForm


def calculations(projects):
    """
    calculate the num_days and percentage_raised for every template
    """
    for p in projects:
        p.percentage = round(((p.raised/p.goal)*100), 1)
        p.num_days = (p.end_date - datetime.now().date()).days


def get_projects(request):
    """
    Create a view that will return a list op Projects
    that were created prior to 'now'
    and render them to the 'projects.html' template
    """
    projects = Project.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date')
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(get_projects)
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            projects = projects.filter(queries)
    
    calculations(projects)
        
    context = {
        'projects': projects,
        'search_term':query,
    }

    return render(request, 'projects.html', context)


def get_project_category(request, project_category):
    """
   per category

    """
    projects = Project.objects.filter(
        category=Category.objects.get(category=project_category).id).order_by('-created_date')
    projects.category = project_category
    
    calculations(projects)
    offset = 2
    paginator = Paginator(projects,offset)
    
    if request.GET.get('page') == None:
        page_number = int(1)
    else:
        page_number = request.GET.get('page')
    
    slice_num = int(page_number)*offset
    print("page_number: ",page_number)
    page_obj = paginator.get_page(page_number)
    print("page_obj: ",page_obj)
    print("slice_num: ",slice_num)
    print("offset: ",slice_num-offset)

    
    context = {
        'projects': projects,
        'page_number': page_number,
        'page_obj': page_obj,
        'slice_num': slice_num,
        'page_start': slice_num-offset,


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
            project = form.save()
            return redirect(project_detail, project.pk)
    else:
        form = StartProjectForm(instance=project)
    
    context = {
        'form': form,
    }
    return render(request, 'startprojectform.html', context)
