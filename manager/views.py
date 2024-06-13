from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from manager.models import Worker, Task


def index(request) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_not_completed_tasks = Task.objects.filter(is_completed=False).count()
    num_not_completed_fast_track_tasks = Task.objects.filter(
        is_completed=False,
        priority="Fast Track"
    ).count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_not_completed_tasks": num_not_completed_tasks,
        "num_not_completed_fast_track_tasks": num_not_completed_fast_track_tasks,
        "num_visits": num_visits,
    }
    return render(request, "manager/index.html", context=context)
