from django.urls import path


from manager.views import (
    index,
    WorkerListView,
    TaskListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("worker/", WorkerListView.as_view(), name="worker"),
    path("task/", TaskListView.as_view(), name="task"),
]

app_name = "manager"
