from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
]