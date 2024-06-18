from django import forms
from django.contrib.auth import get_user_model
from django.forms import CheckboxSelectMultiple

from manager.models import Task


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateField(
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
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


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )
