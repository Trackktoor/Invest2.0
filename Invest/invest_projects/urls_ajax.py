from django.contrib import admin
from django.urls import path
from . import views_ajax

urlpatterns = [
    path('get_all_projects/', views_ajax.GetAllInvestProjects, name='GetAllInvestProjectsAJAX')
]
