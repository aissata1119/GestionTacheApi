from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class TaskHistoryModel(DateTimeModel):
    task = models.ForeignKey('project.TaskModel', related_name='history', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('team.MemberModel', on_delete=models.SET_NULL, null=True)
    progress = models.CharField(max_length=50)


