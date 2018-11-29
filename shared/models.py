from django.db import models
from django.utils import timezone

# Create your models here.

class Notification(models.Model):
    """
    Model representing a single notification
    about traffic from different sources
    """
    title = models.CharField(max_length=60, blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=50)
