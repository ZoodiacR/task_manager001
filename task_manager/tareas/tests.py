from django.test import TestCase
from tareas.models import Task
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task




class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(title='Test Task', description='This is a test task')

    def test_task_creation(self):
        task = Task.objects.get(title='Test Task')
        self.assertEqual(task.description, 'This is a test task')




class TaskViewSetTest(APITestCase):
    def test_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
