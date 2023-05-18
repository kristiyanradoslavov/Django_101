from django.contrib import admin
from django_101.Tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "description", "name", "priority"]


admin.site.register(Task, TaskAdmin)
