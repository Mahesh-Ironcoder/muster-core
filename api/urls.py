import imp
from django.urls import path

urlpatterns = [
    path('spaces/'),
    path('spaces/<int:id>/'), 
    path('spaces/create/'),
    path('spaces/update/<int:id>/'),
    path('spaces/delete/<int:id>/')
]