from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class PostQuerySet(models.QuerySet):
    """
    Represents a queryset functions
    """
    def published(self):
        return self.filter(status=self.model.PUBLISHED)

    def drafts(self):
        return self.filter(status=self.model.DRAFT)

    # def get_authors(self):
    #     User = get_user_model()
    #     # Get the users who are authors of this queryset
    #     return User.objects.filter(blog_posts__in=self).distinct()

class Artigo(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_posts',
        null=False,
    )
    titulo = models.CharField(max_length=299)
    imagem = models.ImageField(
        blank=True,
        null=True,
        help_text='A image for your artigo'
    )
    texto = RichTextUploadingField()
    submitted = models.DateTimeField(auto_now_add=True)
    destaque = models.BooleanField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_artigos',
        null=True,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )

    objects = PostQuerySet.as_manager()


    class Meta:
        ordering = ['-submitted']

    def get_absolute_url(self):
        # if self.submitted:
        #     kwargs = {
        #         'year': self.submitted.year,
        #         'month': self.submitted.month,
        #         'day': self.submitted.day,
        #     }
        # else:
        kwargs = {'pk': self.pk}

        return reverse('artigo-detail', kwargs=kwargs)

    def __str__(self):
        return self.titulo

