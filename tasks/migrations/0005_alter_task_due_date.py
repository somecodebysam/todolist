# Generated by Django 5.0.7 on 2024-08-11 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_author_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.date(2024, 9, 10), help_text='Enter a date in the future', verbose_name='Due Date'),
        ),
    ]
