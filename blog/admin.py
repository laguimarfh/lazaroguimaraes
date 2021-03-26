from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'imagem',
        'submitted',
        'destaque',
        'author',
    )  
    list_filter = (
        'status',
        'topicos',
    )

@admin.register(models.Topico)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'topico',
        'slug',
    )
    prepopulated_fields = {'slug': ('topico',)}
