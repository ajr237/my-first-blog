from django.db import models
from django.utils import timezone

# Create your models here.

class POST(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
