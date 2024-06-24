from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import TaskType, Position, Task, Worker

admin.site.register(TaskType)
admin.site.register(Position)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                        "email"
                    )
                },
            ),
        )
    )
