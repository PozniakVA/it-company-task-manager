from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import (
    TaskForm,
    TaskAssignDeleteForm,
    TaskSearchForm,
    TaskTypeSearchForm,
    TaskTypeForm,
)
from manager.models import Task, TaskType
from user.models import Worker


def index(request) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_not_completed_tasks = Task.objects.filter(
        is_completed=False
    ).count()
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
    return render(
        request,
        "manager/index.html",
        context=context
    )


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task")

    def get_context_data(self, **kwargs: object) -> object:
        context = super().get_context_data(**kwargs)
        context["title"] = "Create task"
        return context


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task")

    def get_context_data(self, **kwargs: object) -> object:
        context = super().get_context_data(**kwargs)
        context["title"] = "Update task"
        return context


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "manager/task_type_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        form = TaskTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "manager/task_type_form.html"
    context_object_name = "task_type"
    success_url = reverse_lazy("manager:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "manager/task_type_form.html"
    context_object_name = "task_type"
    success_url = reverse_lazy("manager:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "manager/task_type_confirm_delete.html"
    context_object_name = "task_type"
    success_url = reverse_lazy("manager:task-type-list")


class AssignDeleteUserToTaskView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Task
    form_class = TaskAssignDeleteForm

    def get_context_data(self, **kwargs: object) -> object:
        context = super().get_context_data(**kwargs)
        context["title"] = "Assign task to workers"
        return context


@login_required
def task_done(request, pk) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse_lazy("manager:task"))
