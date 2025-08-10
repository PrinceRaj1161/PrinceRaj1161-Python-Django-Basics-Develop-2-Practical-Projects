# from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    task = Task.objects.filter(is_completed = False)
    completed_task = Task.objects.filter(is_completed = True)
    context = {
        "tasks" : task, 
        "completed_task" : completed_task
    }
    return render(request, "home.html", context)