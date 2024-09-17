from base.models.helpers.date_time_model import DateTimeModel
from django.db import models


class SummonsModel(DateTimeModel):
    task = models.ForeignKey('project.TaskModel', on_delete=models.CASCADE, related_name='summons')
    member = models.ForeignKey('team.MemberModel', on_delete=models.CASCADE, related_name="summons", null=True)
    assigned_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()

