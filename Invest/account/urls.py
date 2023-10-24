from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.Sugnup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate, name='activate'), 
    path('<int:user_id>', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout')
]
