from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from user.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="ErenAdmin",
            password="12345",
        )
        self.client.force_login(self.admin_user)
        position = Position.objects.create(
            name="Manager"
        )
        self.worker = get_user_model().objects.create_user(
            username="Levi",
            password="12345",
            position=position
        )

    def test_worker_position_listed(self) -> None:
        url = reverse("admin:user_worker_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)

    def test_worker_detail_position_listed(self) -> None:
        url = reverse("admin:user_worker_change", args=[self.worker.id])
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)

    def test_worker_add_position_listed(self) -> None:
        url = reverse("admin:user_worker_add")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)
