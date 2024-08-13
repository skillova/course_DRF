from rest_framework import serializers

from habits.models import Habits
from habits.validators import RewardValidator, RelatedHabitValidator, ExecutionTimeValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'
        validators = (
            RewardValidator(field='reward'),
            RelatedHabitValidator(field='related_habit'),
            ExecutionTimeValidator(field='time_to_complete'),
        )
