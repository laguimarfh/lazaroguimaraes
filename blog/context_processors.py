from django.db.models import Count
from . import models


def base_context(request):
    artigos_ultimos = models.Artigo.objects.filter(status='published')[:4]
    artigos = models.Artigo.objects.filter(status='published')
    artigo_destaque = models.Artigo.objects.filter(destaque=True)
    return {
        'artigos_ultimos': artigos_ultimos,
        'artigo_destaque': artigo_destaque,
        'artigos': artigos,
    }
