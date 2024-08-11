from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .permissions import IsOwner
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework import generics


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserListAPIView(generics.ListAPIView):
    """ Список пользователей """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, IsAdminUser)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Обновление пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class MyTokenObtainPairView(TokenObtainPairView):
    """ Создание токена """
    serializer_class = MyTokenObtainPairSerializer
