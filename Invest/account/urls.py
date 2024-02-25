from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from . import views_ajax

urlpatterns = [
    path('', views.Sugnup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'), 
    path('<int:user_id>', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('my_projects/', views.my_projects, name='my_projects'),
    path('ajax/', include('account.urls_ajax'),)
]