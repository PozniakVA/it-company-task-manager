from django.contrib.auth.models import AbstractUser

from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("user:position-detail", kwargs={'pk': self.pk})


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("user:worker-detail", kwargs={"pk": self.pk})
