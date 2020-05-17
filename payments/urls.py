from django.conf.urls import url
from .views import funding

urlpatterns = [
    url(r'^$', funding, name="funding"),

]