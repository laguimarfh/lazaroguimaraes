from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home2/', views.HomeView2.as_view(), name='home2'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('artigos/', views.ArtigoListView.as_view(), name='artigo-list'),
    path(
        'artigos/<int:pk>/',
        views.ArtigoDetailView.as_view(),
        name='artigo-detail',
    ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]