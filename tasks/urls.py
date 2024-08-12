from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('todo', views.index, name='list'),
    path('todo/<int:pk>', views.task_details, name='details')
]
