from django.urls import path

from habits.views import HabitsCreateAPIView, HabitsListAPIView, HabitsRetrieveAPIView, HabitsUpdateAPIView, \
    HabitsDestroyAPIView
from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('create/', HabitsCreateAPIView.as_view(), name='habits-create'),
    path('list/', HabitsListAPIView.as_view(), name='habits-list'),
    path('get/<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habits-get'),
    path('update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habits-update'),
    path('delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habits-delete'),
]