from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:pk>', views.task_details, name='details')
]
