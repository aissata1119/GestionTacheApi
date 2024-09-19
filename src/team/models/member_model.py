from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class MemberModel(NamedDateTimeModel):
    team = models.ForeignKey('team.TeamModel', on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return f"{self.name} - Team:{self.team}"
