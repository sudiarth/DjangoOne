from django.db import models
from apps.auth_user.models import User

class BillItem(models.Model):

    description = models.CharField(max_length=64, unique=True)
    amount = models.FloatField()

    user = models.ForeignKey(User, related_name='bills', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)