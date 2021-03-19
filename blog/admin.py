from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'imagem',
        'texto',
        'submitted',
    )