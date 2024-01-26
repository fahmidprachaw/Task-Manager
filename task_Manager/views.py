from django.shortcuts import render, redirect
from task.models import Task


def Home(request):
    data = Task.objects.all()
    return render(request, 'index.html', {'data': data})
