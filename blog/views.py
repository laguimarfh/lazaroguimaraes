from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView
from . import models

# Create your views here.


class HomeView(TemplateView):
    """
    The blog home
    """
    template_name = 'blog/home.html'
    def get_context_data (self, **kwargs):
    # Get the parent context
        context = super().get_context_data(**kwargs)
        ultimos_artigos = models.Artigo.objects.all()
    
        context.update({'ultimos_artigos': ultimos_artigos})
        return context


class AboutView(TemplateView):
    """
    The blog About
    """
    template_name = 'blog/about.html'

class ArtigoListView(ListView):
    model = models.Artigo
    context_object_name = 'artigos'

class ArtigoDetailView(DetailView):
    model = models.Artigo
    context_object_name = 'artigos'

    def get_queryset(self):
        queryset = super().get_queryset().published()

        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        # Otherwise, filter on the published date
        return queryset.filter(
            submitted__year=self.kwargs['year'],
            submitted__month=self.kwargs['month'],
            submitted__day=self.kwargs['day'],
        )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Get the post object
    #     artigo = self.get_object()

    #     # Set the post field on the form
    #     comment_form = forms.CommentForm(initial={'post': post})
    #     comments = models.Comment.objects.filter(post=post)
    #     # like = models.Comment.objects.filter(id=10)
    #     # like.update(likes= F('likes') + 1)

    #     context['comment_form'] = comment_form
    #     context['comments'] = comments.order_by('-created')
    #     # context['like'] = like

    #     return context
