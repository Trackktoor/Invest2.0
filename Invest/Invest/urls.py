from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invest_projects.urls')),
    path('account/', include('account.urls'))
]
