from rest_framework import serializers
from project.models.summons_model import SummonsModel


class SummonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SummonsModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'update_at']
