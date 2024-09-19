from base.models.helpers.date_time_model import DateTimeModel
from django.conf import settings
from django.db import models
from history.models.task_history_model import TaskHistoryModel
from rest_framework.exceptions import ValidationError
from django.core.mail import send_mail


class SummonsModel(DateTimeModel):
    task = models.ForeignKey('project.TaskModel', on_delete=models.CASCADE, related_name='summons')
    member = models.ForeignKey('team.MemberModel', on_delete=models.CASCADE, related_name="summons")
    assigned_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()

    def __str__(self):
        return f" Tâche {self.task.title} assigné à {self.member.name}"

    def clean(self):
        project = self.task.project

        assigned_tasks = SummonsModel.objects.filter(task__project=project)

        if not assigned_tasks.exists():
            return
        else:
            team = self.member.team
            has_team_member_assigned = assigned_tasks.filter(member__team=team).exists()

            if not has_team_member_assigned:
                raise ValidationError("Vous n'êtes sur ce projet.")

            assigned_to_member = assigned_tasks.filter(member=self.member).exists()

            if not assigned_to_member:
                raise ValidationError("La tâche est  déja à une personne.")

            # already_assigned = SummonsModel.objects.filter(task=self.task, member=self.member).exists()
            #
            # if already_assigned:
            #     raise ValidationError("Cette tâche est déjà assignée à cette personne.")

            unfinished_tasks = SummonsModel.objects.filter(member=self.member).exclude(task__progress='done')

            if unfinished_tasks.exists():
                raise ValidationError("Cette personne a déjà une tâche en cours.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        progress = TaskHistoryModel.objects.create(
            task=self.task.title,
            updated_by=self.member.name,
            progress=f" Tâche {self.task.title} du projet {self.task.project.name}  assignée à {self.member.name}"
        )
        send_notif_email(progress.progress)


def send_notif_email(message_text):
    subject = 'Email de notification'
    message = message_text
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['ptrece8@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
