from rest_framework import serializers

from habits.models import Habits
from habits.validators import RewardValidator, RelatedHabitValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'
        validators = (
            RewardValidator(field='reward'),
            RelatedHabitValidator(field='related_habit'),
        )
