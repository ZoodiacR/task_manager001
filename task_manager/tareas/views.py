
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import filters
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated,permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'creation_date']



    @api_view(['GET'])
    def task_list(request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def send_task_notification_email(user_email, task_title):
        subject = 'Task Notification'
        message = render_to_string('task_notification_email.html', {'task_title': task_title})
        send_mail(subject, message, 'andyleon000820@gmail.com', [user_email])
