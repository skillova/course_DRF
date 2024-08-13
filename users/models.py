from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    NULLABLE = {
        'null': True,
        'blank': True
    }
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email пользователя'
    )
    tg_chat_id = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name='Телеграмм chat-id'
    )

    # Строка, описывающая имя поля в модели пользователя, которая используется в качестве уникального идентификатора
    USERNAME_FIELD = 'email'

    # Список имен полей, которые будут запрошены при создании пользователя с помощью createsuperuser команды управления
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
