from django.urls import path
from . import views



urlpatterns = [
    path('list_convertclient/', views.listclients, name = 'upload-list-clients'),
    path('list_convertmatters/', views.listmatters, name = 'upload-list-matters'),
    path('list_converttask/', views.listtask, name = 'upload-list-tasks'),
]
