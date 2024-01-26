from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def add_task(request):
    if request.method == 'POST':
        tast_form = forms.TaskForm(request.POST)
        if tast_form.is_valid():
            tast_form.save()
            return redirect('add_task')
    else:
        tast_form = forms.TaskForm()
    return render(request, 'task/add_task.html', {'form': tast_form})



def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    tast_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        tast_form = forms.TaskForm(request.POST, instance=task)
        if tast_form.is_valid():
            tast_form.save()
            return redirect('homepage')
        
    return render(request, 'task/add_task.html', {'form': tast_form})


def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('homepage')
