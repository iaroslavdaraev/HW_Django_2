from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Ссылка')
    text = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    creation_date = models.DateField(auto_now_add=True)
    published = models.BooleanField(verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return f'Blog post "{self.title}" ({self.slug})'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ('id', 'title')
