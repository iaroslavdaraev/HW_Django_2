from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'Категория {self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True, **NULLABLE)
    updated_at = models.DateField(auto_now=True, **NULLABLE)


    def __str__(self):
        return f'Товар {self.name} в {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
