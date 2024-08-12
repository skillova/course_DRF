from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):
    """ Тестирование модели Habits """

    def setUp(self):
        """ Создание тестовой модели Пользователя (с авторизацией) и Привычки """

        self.user = User.objects.create(
            email="test@test.test",
            password="test"
        )
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            user=self.user,
            place="Магазин",
            execution_time="18:00:00",
            action="Пойти в магазин за покупками",
            time_to_complete=60,
            sign_of_a_pleasant_habit=True,
            frequency_of_execution='every_week',
            is_published=True,
        )

    def test_create_habit(self):
        """ Тестирование создания привычки """

        url = reverse("habits:habits-create")
        data = {
            "user": self.user.pk,
            "place": "Магазин",
            "execution_time": "18:00:00",
            "action": "Пойти в магазин за покупками",
            "time_to_complete": 60,
            "sign_of_a_pleasant_habit": True,
            "frequency_of_execution": 'every_week',
        }

        response = self.client.post(url, data=data)
        data = response.json()
        # print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("user"), self.user.pk)
        self.assertEqual(data.get("place"), "Магазин")
        self.assertEqual(data.get("execution_time"), "18:00:00")
        self.assertEqual(data.get("action"), "Пойти в магазин за покупками")
        self.assertEqual(data.get("time_to_complete"), 60)
        self.assertEqual(data.get("sign_of_a_pleasant_habit"), True)
        self.assertEqual(data.get("frequency_of_execution"), 'every_week')

    def test_list_habit(self):
        """ Тестирование вывода всех привычек """

        response = self.client.get(reverse('habits:habits-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        """ Тестирование просмотра одной привычки """

        url = reverse("habits:habits-get", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        # print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("user"), self.habit.user.id)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("execution_time"), self.habit.execution_time)
        self.assertEqual(data.get("action"), self.habit.action)
        self.assertEqual(data.get("time_to_complete"), self.habit.time_to_complete)
        self.assertEqual(data.get("sign_of_a_pleasant_habit"), self.habit.sign_of_a_pleasant_habit)
        self.assertEqual(data.get("frequency_of_execution"), self.habit.frequency_of_execution)

    def test_update_habit(self):
        """ Тестирование изменений привычки """

        url = reverse("habits:habits-update", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "Фитнес-зал",
            "execution_time": "18:00:00",
            "action": "Тренировка в фитнес-зале",
            "time_to_complete": 120,
            "sign_of_a_pleasant_habit": True,
            "frequency_of_execution": 'everyday',
        }
        response = self.client.put(url, data)
        data = response.json()
        # print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("user"), self.habit.user.id)
        self.assertEqual(data.get("place"), "Фитнес-зал")
        self.assertEqual(data.get("execution_time"), "18:00:00")
        self.assertEqual(data.get("action"), "Тренировка в фитнес-зале")
        self.assertEqual(data.get("time_to_complete"), 120)
        self.assertEqual(data.get("sign_of_a_pleasant_habit"), True)
        self.assertEqual(data.get("frequency_of_execution"), 'everyday')

    def test_delete_habit(self):
        """ Тестирование удаления привычки """

        url = reverse("habits:habits-delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
