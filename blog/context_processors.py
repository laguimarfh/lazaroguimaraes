from django.db.models import Count
from . import models


def base_context(request):
    artigos = models.Artigo.objects.filter(status='published')   
    
    return {
        'artigos': artigos,
    }
