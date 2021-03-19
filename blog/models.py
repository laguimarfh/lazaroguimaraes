from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(
        blank=True,
        null=True,
        help_text='A image for your artigo'
    )
    texto = RichTextUploadingField()
    submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted']

    def __str__(self):
        return self.titulo

