import datetime

from django.db import models
from authapp.models import UserProfile


class CategoryTypes(models.Model):
    """Модель категорий изображений"""
    category = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        verbose_name='Категория')

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Artworks(models.Model):
    """Модель изображений"""
    CHOICES_STATUS = [('Drf', 'Черновик'),
                      ('Pub', 'Опубликовано'),
                      ('Del', 'Удалено')]
    artwork = models.ImageField(upload_to='artworks/')
    id_author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор')
    id_category = models.ForeignKey(
        CategoryTypes,
        on_delete=models.PROTECT,
        verbose_name='Категория')
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Наименование работы')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание работы')
    status = models.CharField(
        max_length=3,
        choices=CHOICES_STATUS,
        default='Pub')
    date_create = models.DateTimeField(
        # default=datetime.datetime.now(),
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    date_update = models.DateTimeField(
        # default=datetime.datetime.now(),
        auto_now=True,
        verbose_name='Дата обновления'
    )
