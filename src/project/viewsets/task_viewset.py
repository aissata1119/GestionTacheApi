from django.http import JsonResponse
from rest_framework import viewsets
from project.serializers.task_serializer import TaskSerializer
from project.models.task_model import TaskModel


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.filter(status=True)
    serializer_class = TaskSerializer
