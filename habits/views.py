from rest_framework import generics
from habits.models import Habits
from habits.serializers import HabitsSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializer


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()


class HabitsDestroyAPIView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
