from django.urls import path


from manager.views import (
    index,
    WorkerListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("worker/", WorkerListView.as_view(), name="worker"),
]

app_name = "manager"
