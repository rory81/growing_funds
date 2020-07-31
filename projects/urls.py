from django.conf.urls import url
from django.urls import path
from .views import get_projects, project_detail, create_or_edit_project, delete_project, get_project_category

urlpatterns = [
    path('', get_projects, name = 'get_projects'),
    path('<int:pk>', project_detail, name = 'project_detail'),
    path('new/', create_or_edit_project, name = 'start_project'),
    path('<int:pk>/edit/', create_or_edit_project, name = 'edit_project'),
    path('<int:pk>/delete/<str:profile.html>', delete_project, name = 'delete_project'),
    path('category=<str:project_category>', get_project_category, name = 'per_category'),

]
