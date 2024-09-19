from datetime import datetime

from django.http import JsonResponse
from rest_framework import viewsets
from .models.task_history_model import TaskHistoryModel
from .serializers.notification_serializer import NotificationSerializer
from rest_framework.decorators import action
from .pagination import StandardResultsSetPagination


# Create your views here.
class Notification(viewsets.ModelViewSet):
    queryset = TaskHistoryModel.objects.all()
    serializer_class = NotificationSerializer
    http_method_names = ['get']
    pagination_class = StandardResultsSetPagination

    @action(detail=False)
    def today_notif(self, request):
        today = datetime.today().date()
        queryset = TaskHistoryModel.objects.filter(created_at__date=today)
        serializer = NotificationSerializer(queryset, many=True)
        response_data = {
            'date': today,
            'notifications': serializer.data
        }
        return JsonResponse(response_data, safe=False, status=200)

    @action(detail=False)
    def day_notif(self, request):
        date_query = self.request.GET.get('date')
        queryset = TaskHistoryModel.objects.filter(created_at__date=date_query)
        serializer = NotificationSerializer(queryset, many=True)
        response_data = {
            'date': date_query,
            'notifications': serializer.data
        }
        return JsonResponse(response_data, safe=False, status=200)
