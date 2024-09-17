from rest_framework import serializers
from team.models.team_model import TeamModel


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'update_at']


class TeamMemberSerializer(serializers.ModelSerializer):
    team_member = serializers.StringRelatedField(many=True, read_only=True, source='members')

    class Meta:
        model = TeamModel
        fields = ['team_member']
