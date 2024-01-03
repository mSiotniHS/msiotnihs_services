from django.db import models


class Wish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='uploads', verbose_name='Изображение')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'
