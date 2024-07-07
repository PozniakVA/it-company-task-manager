from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from user.models import Worker, Position


class PublicWorkerTest(TestCase):
    def test_login_required_worker_list_view(self) -> None:
        response = self.client.get(reverse("user:worker"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_worker_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "user:worker-detail",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)


class PublicPositionTest(TestCase):
    def test_login_required_position_list_view(self) -> None:
        response = self.client.get(reverse("user:position"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_position_create_view(self) -> None:
        response = self.client.get(reverse("user:position-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_position_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "user:position-detail",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_position_update_view(self) -> None:
        response = self.client.get(
            reverse(
                "user:position-update",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_position_delete_view(self) -> None:
        response = self.client.get(
            reverse(
                "user:position-delete",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Eren",
            password="12345",
        )
        self.client.force_login(self.user)

        Position.objects.create(
            name="Test1",
        )
        Position.objects.create(
            name="Test2",
        )

        get_user_model().objects.create(
            username="Test1",
            password="password1"
        )


class PrivateWorkerTest(BaseTestCase):
    def test_retrieve_task_list_view(self) -> None:
        response = self.client.get(reverse("user:worker"))
        self.assertEqual(response.status_code, 200)

        worker = Worker.objects.all()
        self.assertEqual(
            list(response.context["worker_list"]),
            list(worker)
        )

        self.assertTemplateUsed(response, "user/worker_list.html")

    def test_retrieve_task_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "user:worker-detail", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "user/worker_detail.html")

    def test_task_list_view_search(self) -> None:
        # Checking that all tasks are displayed
        response = self.client.get(reverse("user:worker"))
        self.assertEqual(len(response.context["object_list"]), 2)

        # Checking that only one task is found
        response = self.client.get(
            reverse("user:worker"), {"username": "Test1"}
        )
        self.assertEqual(len(response.context["object_list"]), 1)

        # Checking that nothing was found
        response = self.client.get(
            reverse("user:worker"), {"username": "Test -3"}
        )
        self.assertEqual(len(response.context["object_list"]), 0)


class PrivatePositionTest(BaseTestCase):
    def test_retrieve_position_list_view(self) -> None:
        response = self.client.get(reverse("user:position"))
        self.assertEqual(response.status_code, 200)

        position = Position.objects.all()
        self.assertEqual(
            list(response.context["position_list"]),
            list(position)
        )

        self.assertTemplateUsed(response, "user/position_list.html")

    def test_retrieve_position_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "user:position-detail", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "user/position_detail.html")

    def test_retrieve_position_create_view(self) -> None:
        response = self.client.get(reverse("user:position-create"))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "user/position_form.html")

    def test_retrieve_position_delete_view(self) -> None:
        response = self.client.get(
            reverse(
                "user:position-delete", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "user/position_confirm_delete.html")

    def test_task_type_list_view_search(self) -> None:
        # Checking that all tasks are displayed
        response = self.client.get(reverse("user:position"))
        self.assertEqual(len(response.context["object_list"]), 2)

        # Checking that only one task is found
        response = self.client.get(reverse("user:position"), {"name": "Test1"})
        self.assertEqual(len(response.context["object_list"]), 1)

        # Checking that nothing was found
        response = self.client.get(
            reverse("user:position"), {"name": "Test -3"}
        )
        self.assertEqual(len(response.context["object_list"]), 0)
