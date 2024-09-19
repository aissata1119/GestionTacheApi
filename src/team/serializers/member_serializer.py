from rest_framework import serializers
from team.models.member_model import MemberModel


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']


class MemberTaskSerializer(serializers.ModelSerializer):
    summons = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='task.title'
    )

    class Meta:
        model = MemberModel
        fields = ['id', 'name', 'summons']
