from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from project.models.summons_model import SummonsModel
from history.models.task_history_model import TaskHistoryModel



class TaskModel(DateTimeModel):
    project = models.ForeignKey('project.ProjectModel', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=30)
    progress = models.CharField(max_length=50, choices=[
        ('todo', 'To Do'), ('in_progress', 'IN PROGRESS'), ('done', 'Done')
    ])

    def __str__(self):
        return f"{self.id}:{self.title}"

    def save(self, *args, **kwargs):
        if self.pk:
            task = TaskModel.objects.get(pk=self.pk)
            summons = SummonsModel.objects.get(task=self.pk)
            member = summons.member
            if task.progress != self.progress:
                TaskHistoryModel.objects.create(
                    task=task,
                    updated_by=member,
                    progress=f"Statut de la tâche modifié de {previous.progress} à {self.progress}"
                )

        super().save(*args, **kwargs)
