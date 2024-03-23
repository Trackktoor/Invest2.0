from django.contrib import admin
from django.urls import path
from . import views_ajax

urlpatterns = [
    path('delete_project/<int:user_id>/<int:project_id>/', views_ajax.delete_project, name='delete_project'),
]
