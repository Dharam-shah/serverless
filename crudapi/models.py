from django.db import models
from datetime import datetime 

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    deadline = models.DateTimeField(blank=True)

