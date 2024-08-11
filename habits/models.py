from django.db import models

from config import settings


class Habits(models.Model):
    NULLABLE = {
        'null': True,
        'blank': True
    }
    SIGN_OF_A_PLEASANT_HABIT_CHOICES = (
        (True, 'Полезная привычка'),
        (False, 'Вредная привычка'),
    )
    FREQUENCY_OF_EXECUTION_CHOICES = (
        ('everyday', 'Ежедневно'),
        ('every_week', 'Еженедельно'),
    )
    IS_PUBLISH = (
        (True, 'Опубликовано'),
        (False, 'Не опубликовано'),
    )

    place = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name='Место'
    )
    execution_time = models.TimeField(
        verbose_name='Время'
    )
    action = models.CharField(
        max_length=250,
        **NULLABLE,
        verbose_name='Действие'
    )
    sign_of_a_pleasant_habit = models.BooleanField(
        choices=SIGN_OF_A_PLEASANT_HABIT_CHOICES,
        verbose_name='Признак приятной привычки'
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Связанная привычка'
    )
    frequency_of_execution = models.CharField(
        max_length=80,
        choices=FREQUENCY_OF_EXECUTION_CHOICES,
        default='everyday',
        verbose_name='Периодичность'
    )
    reward = models.CharField(
        max_length=250,
        **NULLABLE,
        verbose_name='Вознаграждение'
    )
    time_to_complete = models.SmallIntegerField(
        verbose_name='Время на выполнение'
    )
    is_published = models.BooleanField(
        choices=IS_PUBLISH,
        default=False,
        verbose_name='Признак публичности'
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name='Пользователь '
    )

    def __str__(self):
        return f'Я буду {self.action} в {self.execution_time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
