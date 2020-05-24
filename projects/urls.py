from django.conf.urls import url
from .views import get_projects, project_detail, create_or_edit_project, get_project_category


urlpatterns = [
    url(r'^$', get_projects, name = 'get_projects'),
    url(r'^(?P<pk>\d+)/$', project_detail, name = 'project_detail'),
    url(r'^new/$', create_or_edit_project, name = 'start_project'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_project, name = 'edit_project'),
    url(r'^category=(?P<project_category>\w+)$', get_project_category, name = 'per_category'),
    
]
