# Generated by Django 5.1.4 on 2024-12-07 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
