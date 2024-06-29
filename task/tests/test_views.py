from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task.models import Task, TaskType


class PublicTaskTest(TestCase):
    def test_login_required_task_list_view(self) -> None:
        response = self.client.get(reverse("task:task"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_create_view(self) -> None:
        response = self.client.get(reverse("task:task-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-detail",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_update_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-update",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_delete_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-delete",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)


class PublicTaskTypeTest(TestCase):
    def test_login_required_task_type_list_view(self) -> None:
        response = self.client.get(reverse("task:task-type-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_type_create_view(self) -> None:
        response = self.client.get(reverse("task:task-type-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_type_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-type-detail",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_type_update_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-type-update",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_type_delete_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-type-delete",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)


class PublicAssignDeleteUserToTaskTest(TestCase):
    def test_login_required_assign_delete_user_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-assign-delete",
                kwargs={"pk": 1}
            )
        )
        self.assertNotEqual(response.status_code, 200)


class PublicTaskDoneTest(TestCase):
    def test_login_required_task_done_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-done",
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
        deadline = datetime.now() + timedelta(days=7)
        self.task_type_1 = TaskType.objects.create(name="Task Type 1")
        self.task_type_2 = TaskType.objects.create(name="Task Type 2")
        Task.objects.create(
            name="Task1",
            description="Description1",
            deadline=deadline,
            task_type=self.task_type_1,
        )
        Task.objects.create(
            name="Task2",
            description="Description2",
            deadline=deadline,
            task_type=self.task_type_2,
        )


class PrivateTaskTest(BaseTestCase):
    def test_retrieve_task_list_view(self) -> None:
        response = self.client.get(reverse("task:task"))
        self.assertEqual(response.status_code, 200)

        task = Task.objects.all()
        self.assertEqual(
            list(response.context["task_list"]),
            list(task)
        )

        self.assertTemplateUsed(response, "task/task_list.html")

    def test_retrieve_task_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-detail", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_detail.html")

    def test_retrieve_task_create_view(self) -> None:
        response = self.client.get(reverse("task:task-create"))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_form.html")

    def test_retrieve_task_update_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-update", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_form.html")

    def test_retrieve_task_delete_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-delete", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_confirm_delete.html")

    def test_task_list_view_search(self) -> None:
        # Checking that all tasks are displayed
        response = self.client.get(reverse("task:task"))
        self.assertEqual(len(response.context["object_list"]), 2)

        # Checking that only one task is found
        response = self.client.get(reverse("task:task"), {"name": "Task1"})
        self.assertEqual(len(response.context["object_list"]), 1)

        # Checking that nothing was found
        response = self.client.get(reverse("task:task"), {"name": "Task -3"})
        self.assertEqual(len(response.context["object_list"]), 0)


class PrivateTaskTypeTest(BaseTestCase):
    def test_retrieve_task_type_list_view(self) -> None:
        response = self.client.get(reverse("task:task-type-list"))
        self.assertEqual(response.status_code, 200)

        task_type = TaskType.objects.all()
        self.assertEqual(
            list(response.context["task_type_list"]),
            list(task_type)
        )

        self.assertTemplateUsed(response, "task/task_type_list.html")

    def test_retrieve_task_type_detail_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-type-detail", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_type_detail.html")

    def test_retrieve_task_type_create_view(self) -> None:
        response = self.client.get(reverse("task:task-type-create"))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_type_form.html")

    def test_retrieve_task_type_delete_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-type-delete", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_type_confirm_delete.html")

    def test_task_type_list_view_search(self) -> None:
        # Checking that all tasks are displayed
        response = self.client.get(reverse("task:task-type-list"))
        self.assertEqual(len(response.context["object_list"]), 2)

        # Checking that only one task is found
        response = self.client.get(reverse("task:task-type-list"), {"name": "Task Type 1"})
        self.assertEqual(len(response.context["object_list"]), 1)

        # Checking that nothing was found
        response = self.client.get(reverse("task:task-type-list"), {"name": "Task Type -3"})
        self.assertEqual(len(response.context["object_list"]), 0)


class PrivateAssignDeleteUserToTaskTest(BaseTestCase):
    def test_retrieve_assign_delete_user_to_task_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-assign-delete", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "task/task_form.html")


class PrivateTaskDoneTest(BaseTestCase):
    def test_retrieve_task_done_view(self) -> None:
        response = self.client.get(
            reverse(
                "task:task-done", kwargs={"pk": 1}
            )
        )
        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse("task:task"))
