from django.urls import path

from user.views import (
    WorkerListView,
    WorkerDetailView,
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
)

urlpatterns = [
    path(
        "worker/",
        WorkerListView.as_view(),
        name="worker"
    ),
    path(
        "worker/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "position/",
        PositionListView.as_view(),
        name="position"
    ),
    path(
        "position/<int:pk>/",
        PositionDetailView.as_view(),
        name="position-detail"
    ),
    path(
        "position/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "position/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete"
    ),
]

app_name = "user"
