from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.


class HomeView(TemplateView):
    """
    The blog home
    """
    template_name = 'blog/home.html'



class AboutView(TemplateView):
    """
    The blog About
    """
    template_name = 'blog/about.html'