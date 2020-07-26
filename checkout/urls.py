from django.urls import path
from .views import checkout, charge
# , success


urlpatterns = [
    path('<int:pk>', checkout, name='checkout'),
    path('<int:pk>/charge', charge, name='charge'),
    # path('success/<int:total>/<int:pk>/<str:order_number>', success, name='success'),
]
