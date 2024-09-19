from rest_framework import serializers
from history.models.task_history_model import TaskHistoryModel


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistoryModel
        fields = ['progress']
        read_only_fields = ['progress']
