from rest_framework import serializers

from project.models.project_model import ProjectModel
from project.serializers.task_serializer import TaskSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'update_at']


class ProjectTaskSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField(many=True, read_only=True, source="tasks")

    class Meta:
        model = ProjectModel
        fields = ['task']
