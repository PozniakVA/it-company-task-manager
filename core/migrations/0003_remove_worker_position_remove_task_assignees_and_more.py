# Generated by Django 5.0.6 on 2024-06-28 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_worker_position"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="worker",
            name="position",
        ),
        migrations.RemoveField(
            model_name="task",
            name="assignees",
        ),
        migrations.RemoveField(
            model_name="task",
            name="task_type",
        ),
        migrations.RemoveField(
            model_name="worker",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="worker",
            name="user_permissions",
        ),
        migrations.DeleteModel(
            name="Position",
        ),
        migrations.DeleteModel(
            name="Task",
        ),
        migrations.DeleteModel(
            name="TaskType",
        ),
        migrations.DeleteModel(
            name="Worker",
        ),
    ]
