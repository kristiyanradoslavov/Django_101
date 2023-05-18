from django.shortcuts import render
from django.http import HttpResponse
from django_101.Tasks.models import Task


def index(request):
    all_tasks = Task.objects.all()

    result = ';'.join(f"{t.name} {t.description} {t.priority}" for t in all_tasks)

    return HttpResponse(result)


def all_the_information(request):
    context_info = {
        "title": "this is the title of my first website",
        "body_man": "this is the body of my first website",
    }

    return render(request, "index.html", context_info)

