from django.contrib import admin

from task.models import TaskType, Task

admin.site.register(TaskType)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
