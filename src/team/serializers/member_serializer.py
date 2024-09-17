from rest_framework import serializers
from team.models.member_model import MemberModel


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'update_at']
