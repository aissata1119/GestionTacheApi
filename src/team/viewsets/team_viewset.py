from django.http import JsonResponse
from rest_framework import viewsets
from team.serializers.team_serializer import TeamSerializer, TeamMemberSerializer
from team.models.team_model import TeamModel
from rest_framework.decorators import action


class TeamViewSet(viewsets.ModelViewSet):
    queryset = TeamModel.objects.filter(status=True)
    serializer_class = TeamSerializer

    @action(detail=True, methods=['get'])
    def member(self, request, pk=None):
        team = self.get_object()
        serializer = TeamMemberSerializer(team)
        return JsonResponse(serializer.data, status=200)
