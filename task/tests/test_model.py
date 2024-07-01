from datetime import datetime, timedelta

from django.test import TestCase

from task.models import Task, TaskType


class TestModel(TestCase):
    def setUp(self) -> None:
        deadline = datetime.now() + timedelta(days=7)
        self.task_type = TaskType.objects.create(name='Task Type')
        self.task = Task.objects.create(
            name="Task",
            description="Description",
            deadline=deadline,
            task_type=self.task_type,
        )

    def test_task_type_str(self) -> None:
        self.assertEqual(str(self.task_type), "Task Type")

    def test_task_str(self) -> None:
        self.assertEqual(str(self.task.name), "Task")
