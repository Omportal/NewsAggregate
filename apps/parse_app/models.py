from django.db import models


class ParseData(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.CharField(max_length=500, verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')
    img_link = models.URLField(verbose_name='Изображение', null=True)

    class Meta:

        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return self.title
