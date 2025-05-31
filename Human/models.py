from django.db import models
from django.template.base import kwarg_re
from django.urls import reverse_lazy

# Create your models here.
class Humans(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return  reverse_lazy('view_human', kwargs={'pk': self.pk})



    class Meta:
      verbose_name = 'Human'
      verbose_name_plural = 'Humans'
      ordering = [ '-created_at' ]

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('Category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

