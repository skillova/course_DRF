from rest_framework import serializers


class RewardValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reward = value.get(self.field)
        related_habit = value.get('related_habit')
        sign_of_a_pleasant_habit = value.get('sign_of_a_pleasant_habit')
        if reward and sign_of_a_pleasant_habit:
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения')
        elif reward and related_habit:
            raise serializers.ValidationError(
                'В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки.')


class RelatedHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get(self.field)
        sign_of_a_pleasant_habit = value.get('sign_of_a_pleasant_habit')
        if related_habit and not related_habit.sign_of_a_pleasant_habit:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.')
        if related_habit and sign_of_a_pleasant_habit:
            raise serializers.ValidationError('У приятной привычки не может быть связанной привычки.')
