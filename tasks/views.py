from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks =  Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)

def task_details(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return HttpResponse(task.title)
