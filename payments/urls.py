from django.conf.urls import url
from .views import funding

urlpatterns = [
    url(r'^$', funding, name="funding"),
    url(r'^(?P<pk>\d+)/$', funding, name = 'funding_project'),

]

