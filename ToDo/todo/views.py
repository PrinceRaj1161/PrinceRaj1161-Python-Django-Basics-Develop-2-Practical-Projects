from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addtask(request):
    task = request.POST['task'] 
    print(task)
    Task.objects.create(task=task)
    return redirect("home")

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True 
    task.save()
    return redirect("home")

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False 
    task.save()
    return redirect("home")

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        newtask = request.POST['task']
        task.task = newtask
        task.save()
        return redirect("home")
    else:
        context = {
            'task' : task,
        }
        return render(request, 'edit.html', context=context)
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")