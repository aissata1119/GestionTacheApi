from rest_framework import serializers
from history.models.task_history_model import TaskHistoryModel


class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistoryModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']