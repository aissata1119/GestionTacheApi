from rest_framework import serializers
from project.models.task_model import TaskModel

from project.models.project_model import ProjectModel


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    project_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=ProjectModel.objects.all(),
                                                    source='project')

    class Meta:
        model = TaskModel
        fields = "__all__"
        read_only_fields = ['id', 'status', 'progress', 'created_at', 'updated_at']



class TaskAssignedSerializer(serializers.ModelSerializer):
    summons = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='member.name'
    )

    class Meta:
        model = TaskModel
        fields = ['summons']
