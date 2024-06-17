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
)

urlpatterns = [
    path("", index, name="index"),
    path("worker/", WorkerListView.as_view(), name="worker"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("task/", TaskListView.as_view(), name="task"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("position/", PositionListView.as_view(), name="position"),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
]

app_name = "manager"
