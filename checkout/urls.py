from django.conf.urls import url
from django.urls import path
from .views import create_session



urlpatterns = [
    
    path('<int:pk>', create_session, name = 'checkout'),    
    
]
