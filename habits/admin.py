from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'action',
        'sign_of_a_pleasant_habit',
        'related_habit',
        'execution_time',
        'time_to_complete',
        'place',
        'reward',
        'frequency_of_execution',
        'is_published',
    )
    list_display_links = (
        'action',
    )
    list_editable = (
        'sign_of_a_pleasant_habit',
        'frequency_of_execution',
        'is_published',
    )
    list_per_page = 10
