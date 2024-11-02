from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.patronymic:
            return f'{self.last_name} {self.first_name} {self.patronymic}'
        else:
            return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
