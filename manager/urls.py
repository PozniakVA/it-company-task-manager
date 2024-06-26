from django.urls import path


from manager.views import (
    index,
    TaskListView,
    TaskTypeListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    AssignDeleteUserToTaskView,
    task_done,
    TaskTypeDetailView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "task/",
        TaskListView.as_view(),
        name="task"
    ),
    path(
        "task/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/assign-delete/",
        AssignDeleteUserToTaskView.as_view(),
        name="task-assign-delete"),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/task-done/",
        task_done,
        name="task-done"),
    path(
        "task-type/",
        TaskTypeListView.as_view(),
        name="task-type-list"
    ),
    path(
        "task-type/<int:pk>/",
        TaskTypeDetailView.as_view(),
        name="task-type-detail"
    ),
    path(
        "task-type/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path(
        "task-type/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update"
    ),
    path(
        "task-type/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete"
    ),
]

app_name = "manager"
