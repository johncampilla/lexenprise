from django.urls import path
from . import views

urlpatterns = [
    path("tmwatch/", views.gazettelist, name='publication-list'),
]