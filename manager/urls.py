from django.urls import path


from manager.views import (
    index,
    WorkerListView,
    TaskListView,
    PositionListView,
    TaskTypeListView,
    WorkerDetailView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    AssignDeleteUserToTaskView,
    task_done,
    PositionCreateView,
    PositionDetailView,
    PositionDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("worker/", WorkerListView.as_view(), name="worker"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("task/", TaskListView.as_view(), name="task"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
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
    path("position/", PositionListView.as_view(), name="position"),
    path("position/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
]

app_name = "manager"
