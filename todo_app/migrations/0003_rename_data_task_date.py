# Generated by Django 4.2.3 on 2023-07-18 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_task_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='data',
            new_name='date',
        ),
    ]
