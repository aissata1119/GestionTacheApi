from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class TaskHistoryModel(DateTimeModel):
    task = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    progress = models.TextField()


