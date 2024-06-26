from django import forms
from django.contrib.auth import get_user_model
from django.forms import CheckboxSelectMultiple

from manager.models import Task, TaskType


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateField(
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],


    )

    class Meta:
        model = Task
        fields = (
            "name",
            "deadline",
            "priority",
            "task_type",
            "description",
            "assignees"
        )


class TaskAssignDeleteForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = ("assignees",)


class TaskTypeForm(forms.ModelForm):

    class Meta:
        model = TaskType
        fields = "__all__"


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by type"})
    )
