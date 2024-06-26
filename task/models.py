from django.db import models

from user.models import Worker


class TaskType(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORITY = (
        ("Low Priority", "Lower urgency"),
        ("Standard", "Normal completion pace"),
        ("Fast Track", "Immediate priority and quick completion")
    )

    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY,
        default="Standard"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks"
    )

    def __str__(self) -> str:
        return self.name
