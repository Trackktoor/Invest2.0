from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AllInvestProjects, name='all_projects'),
    path('project/<int:project_id>', views.Project, name='project'),
    path('add_project/', views.AddProject, name='add_project'),
    path('ajax/', include('invest_projects.urls_ajax'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)