from django.db.models import Count
from . import models


def base_context(request):
    artigos = models.Artigo.objects.filter(status='published')   
    artigo_destaque = models.Artigo.objects.filter(destaque=True)   
    return {
        'artigos': artigos,
        'artigo_destaque': artigo_destaque,
    }
