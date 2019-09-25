from django.db import models
from apps.auth_user.models import User

class Quote(models.Model):
    
    content = models.CharField(max_length=256)

    user = models.ForeignKey(User, related_name='users_quote', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)