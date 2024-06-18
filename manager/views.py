from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm, TaskAssignDeleteForm
from manager.models import Worker, Task, Position, TaskType


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
        "num_not_completed_fast_track_tasks":
            num_not_completed_fast_track_tasks,
        "num_visits": num_visits,
    }
    return render(request, "manager/index.html", context=context)


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 3


class WorkerDetailView(generic.DetailView):
    model = Worker


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create task"
        return context


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update task"
        return context


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task")


class PositionListView(generic.ListView):
    model = Position
    paginate_by = 3


class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "manager/task_type_list.html"
    paginate_by = 3


class AssignDeleteUserToTaskView(generic.UpdateView):
    model = Task
    form_class = TaskAssignDeleteForm

    def get_context_data(self, **kwargs: object) -> object:
        context = super().get_context_data(**kwargs)
        context["title"] = "Assign task to workers"
        return context


def task_done(request, pk) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse_lazy("manager:task"))

