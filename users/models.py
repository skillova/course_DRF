from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email пользователя'
    )

    USERNAME_FIELD = 'email'  # Строка, описывающая имя поля в модели пользователя, которая используется в качестве уникального идентификатора
    REQUIRED_FIELDS = []  # Список имен полей, которые будут запрошены при создании пользователя с помощью createsuperuser команды управления

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
