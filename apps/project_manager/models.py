from django.db import models
from apps.auth_user.models import User

class Project(models.Model):
    
    title = models.CharField(max_length=128)

    user = models.ForeignKey(User, related_name='project_users', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    
    description = models.CharField(max_length=256)

    user = models.ForeignKey(User, related_name='task_users', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='task_projects', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)