from django.db import models


class CategoryTypes(models.Model):
    """Модель категорий изображений"""
    catergory = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        verbose_name='Категория')

    def __str__(self):
        return f'{self.type}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
