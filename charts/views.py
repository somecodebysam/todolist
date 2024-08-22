from django.shortcuts import render
from django.db.models import Count
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def task_chart_view(request):
    task_stats = Task.objects.filter(author=request.user).values('completed').annotate(count=Count('id'))
    
    completed_count = 0
    uncompleted_count = 0

    for stat in task_stats:
        if stat['completed']:
            completed_count += stat['count']  
        else:
            uncompleted_count += stat['count']  
    
    data = {
        'labels': ['Completed', 'Uncompleted'],
        'values': [completed_count, uncompleted_count]
    }
    
    return render(request, 'charts/charts.html', {'chart_data': data})
