from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    PRIORITY = (
        ("Low Priority", "Immediate priority and quick completion"),
        ("Standard", "Normal completion pace"),
        ("Fast Track", "Lower urgency")
    )

    name = models.CharField(max_length=100)
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
        on_delete=models.CASCADE
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks"
    )

    def __str__(self) -> str:
        return self.name
