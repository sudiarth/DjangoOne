from django.db import models

class BillItem(models.Model):

    description = models.CharField(max_length=64, unique=True)
    amount = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)