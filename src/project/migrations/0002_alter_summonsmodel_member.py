# Generated by Django 5.1.1 on 2024-09-17 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summonsmodel',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='summons', to='team.membermodel'),
        ),
    ]
