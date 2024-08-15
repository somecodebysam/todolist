from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks =  Task.objects.all()
    context = {}
    context['tasks'] = tasks
    form = TaskForm()
    context['form'] = form
    
    if request.method == "POST":
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            task = Task.objects.get(id=pk)
            task.delete()
        elif 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = TaskForm(request.POST)
                if form.is_valid():
                    task = form.save(commit=False)
                    task.author = request.user
                    task.save()
            else:
                task = Task.objects.get(id=pk)
                form = TaskForm(request.POST, instance=task)
                if form.is_valid():
                    task = form.save(commit=False)
                    task.author = request.user
                    task.save()
            form = TaskForm()
             
        elif 'complete' in request.POST:
            pk = request.POST.get('complete')
            task = Task.objects.get(id=pk)
            task.completed = True
            task.save()
        elif 'uncomplete' in request.POST:
            pk = request.POST.get('uncomplete')
            task = Task.objects.get(id=pk)
            task.completed = False
            task.save()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            task = Task.objects.get(id=pk)
            form = TaskForm(instance=task)
            context['form'] = form


    
    return render(request, 'tasks/tasks.html', context)

def task_details(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return HttpResponse(task.title)
