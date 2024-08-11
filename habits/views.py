from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from habits.models import Habits
from habits.paginators import Pagination
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer

from .tasks import add


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.user = self.request.user
        new_habits.save()
        add.delay()


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    pagination_class = Pagination
    permission_classes = (AllowAny,)


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser, IsOwner,)
