from django.conf.urls import url
from django.urls import path
from .views import checkout


urlpatterns = [
    
    path('<int:pk>', checkout, name = 'checkout'),
    
    
]
