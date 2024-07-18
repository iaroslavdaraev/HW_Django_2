from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null':True, 'blank':True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', help_text='Введите номер телефона', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', help_text='Название старны', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', help_text='Загрузите картинку', **NULLABLE)
    verified = models.BooleanField(verbose_name='активирован', default=False)
    verification_code = models.CharField(max_length=50, verbose_name="код активации", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
