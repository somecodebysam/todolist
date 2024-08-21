from django.urls import path
from . import views

app_name = 'charts'

urlpatterns = [
    path('overview', views.task_chart_view, name='task_chart')
    
]
