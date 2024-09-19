from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, filters
from project.serializers.task_serializer import TaskSerializer, TaskAssignedSerializer
from project.models.task_model import TaskModel
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.filter(status=True)
    serializer_class = TaskSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ('project',)

    @action(detail=True)
    def member(self, request, pk=None):
        task = self.get_object()
        if task:
            serializer = TaskAssignedSerializer(task)
            return JsonResponse(serializer.data, status=200)
        return HttpResponse(status=404)

    @action(detail=True, methods=['PATCH'])
    def status(self, request, pk=None):
        data = JSONParser().parse(request)
        task = self.get_object()
        if task.progress == "todo":
            response_data = {
                'succes': 'Vous avez changé le status de la tâche: tâche débutée',

            }
            echec_data = {
                'echec': 'MAJ du status échoué',

            }
            serializer = TaskAssignedSerializer(task, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(progress="in_progress")
                return JsonResponse(response_data, status=200)
            return JsonResponse(echec_data, status=400)

        if task.progress == "in_progress":
            response_data = {
                'succes': 'Vous avez changé le status de la tâche: tâche terminée',
            }
            echec_data = {
                'echec': 'MAJ du status échoué',
            }
            serializer = TaskAssignedSerializer(task, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(progress="done")
                return JsonResponse(response_data, status=200)
            return JsonResponse(echec_data, status=400)
