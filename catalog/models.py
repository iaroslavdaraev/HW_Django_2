from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Создатель', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'Товар {self.name} в {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id', 'name')


class Version(models.Model):
    VERSION_CHOICES = ((True, 'активная'), (False, 'не активная'))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(default=1, blank=True, verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Название версии')
    is_current = models.BooleanField(choices=VERSION_CHOICES, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.version_name} {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)


@receiver(post_save, sender=Version)
def set_current_version(sender, instance, **kwargs):
    if instance.is_current:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_current=False)
