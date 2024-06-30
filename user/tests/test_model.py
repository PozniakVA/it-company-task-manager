from django.contrib.auth import get_user_model
from django.test import TestCase

from user.models import Position


class TestModel(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Manager")
        self.worker = get_user_model().objects.create(
            first_name="Test",
            last_name="Worker",
            username="test_worker",
            position=self.position,
            password="12345",
        )

    def test_position_str(self) -> None:
        self.assertEqual(str(self.position), "Manager")

    def test_worker_str(self) -> None:
        self.assertEqual(
            str(self.worker),
            f"{self.worker.username} "
            f"({self.worker.first_name} {self.worker.last_name})"
        )
