from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import generic

from task.forms import (
    TaskForm,
    TaskAssignDeleteForm,
    TaskSearchForm,
    TaskTypeSearchForm,
    TaskTypeForm,
)
from task.models import Task, TaskType


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5

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
    success_url = reverse_lazy("task:task")

    def get_context_data(self, **kwargs: object) -> object:
        context = super().get_context_data(**kwargs)
        context["title"] = "Create task"
        return context


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task")

    def get_context_data(self, **kwargs: object) -> object:
        context = super().get_context_data(**kwargs)
        context["title"] = "Update task"
        return context


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task/task_type_list.html"
    paginate_by = 5

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
    template_name = "task/task_type_detail.html"
    context_object_name = "task_type"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task/task_type_form.html"
    context_object_name = "task_type"
    success_url = reverse_lazy("task:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task/task_type_form.html"
    context_object_name = "task_type"
    success_url = reverse_lazy("task:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task/task_type_confirm_delete.html"
    context_object_name = "task_type"
    success_url = reverse_lazy("task:task-type-list")


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

    success_url = reverse_lazy("task:task")


class TaskDoneView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponseRedirect(reverse_lazy("task:task"))
