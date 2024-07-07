from django import forms

from user.models import Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by position"})
    )
