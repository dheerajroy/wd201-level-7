# Generated by Django 4.0.1 on 2022-02-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_taskchange_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]
