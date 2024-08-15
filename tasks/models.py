from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField('Due Date', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
        