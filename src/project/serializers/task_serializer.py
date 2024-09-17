from rest_framework import serializers
from project.models.task_model import TaskModel


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'update_at']
