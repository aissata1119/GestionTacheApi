from django.db import models

from base.models.helpers.named_date_time_model import NamedDateTimeModel


class ProjectModel(NamedDateTimeModel):
    description = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()
