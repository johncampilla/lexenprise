from django.urls import path
from . import views



urlpatterns = [
    path('list_convertclient', views.listclients, name = 'upload-list'),
]
