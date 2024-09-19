from rest_framework import serializers
from team.models.team_model import TeamModel


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']


class TeamMemberSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True,
    )

    class Meta:
        model = TeamModel
        fields = ['id', 'name', 'members']
