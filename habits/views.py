from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habits
from habits.paginators import Pagination
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """
    serializer_class = HabitsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.user = self.request.user
        new_habits.save()


class HabitsListAPIView(generics.ListAPIView):
    """ Список привычек """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    pagination_class = Pagination
    permission_classes = (IsAuthenticated, IsOwner,)

    def get_queryset(self):
        """ Определяем параметры вывода объектов """
        queryset = Habits.objects.filter(user=self.request.user)
        return queryset


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр привычки """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """ Обновление привычки """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitsPublicListAPIView(generics.ListAPIView):
    """ Вывод списка публичных привычек """

    serializer_class = HabitsSerializer
    pagination_class = Pagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """
        return Habits.objects.filter(is_published=True)
