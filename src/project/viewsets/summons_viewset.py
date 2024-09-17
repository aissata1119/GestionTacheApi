from rest_framework import viewsets, status
from project.serializers.summons_serializer import SummonsSerializer
from project.models.summons_model import SummonsModel
from project.models.task_model import TaskModel
from rest_framework.response import Response
from history.serializers.task_history_serializer import TaskHistorySerializer


class SummonsViewSet(viewsets.ModelViewSet):
    queryset = SummonsModel.objects.filter(status=True)
    serializer_class = SummonsSerializer



