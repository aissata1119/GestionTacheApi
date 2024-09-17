from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from project.serializers.project_serializer import ProjectSerializer, ProjectTaskSerializer
from project.models.project_model import ProjectModel
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination


# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 10

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.filter(status=True)
    serializer_class = ProjectSerializer
    # pagination_class = StandardResultsSetPagination

    @action(detail=True, methods=['get'])
    def task(self, request, pk=None):
        project = self.get_object()
        if project:
            serializer = ProjectTaskSerializer(project)
            return JsonResponse(serializer.data, status=200)
        return HttpResponse(status=404)
