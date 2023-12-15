# Generated by Django 4.2.7 on 2023-12-13 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softdesk_management', '0003_alter_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('problem', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('To Do', 'Todo'), ('In Progress', 'In Progress'), ('Finished', 'Finished')], default='To Do', max_length=11)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=6)),
                ('type', models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature'), ('TASK', 'Task')], max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('attribution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attribution', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softdesk_management.project')),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reporter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]