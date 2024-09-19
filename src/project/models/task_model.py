from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from project.models.summons_model import SummonsModel, send_notif_email
from history.models.task_history_model import TaskHistoryModel


class TaskModel(DateTimeModel):
    project = models.ForeignKey('project.ProjectModel', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=30)
    progress = models.CharField(max_length=50, default="todo", choices=[
        ('todo', 'To Do'), ('in_progress', 'IN PROGRESS'), ('done', 'Done')
    ])

    def __str__(self):
        return f"{self.id}:{self.title}, status:{self.progress}"

    def save(self, *args, **kwargs):
        project = self.project
        assigned_tasks = SummonsModel.objects.filter(task__project=project)
        if self.pk and assigned_tasks.exists():
            task = TaskModel.objects.get(pk=self.pk)
            summons = SummonsModel.objects.filter(task=self.pk).last()
            member = summons.member
            if task.progress != self.progress:
                taskhistory = TaskHistoryModel.objects.create(
                    task=task,
                    updated_by=member,
                    progress=f"Statut de la tâche {task.title} du projet {task.project.name} modifié de {task.progress} à {self.progress}"
                )
                send_notif_email(taskhistory.progress)
        super().save(*args, **kwargs)
