from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    video_id = models.CharField(max_length=255, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.URLField(null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    STATUS_CHOICES = [
        ('successful', 'Successful'),
        ('in_progress', 'In Progress'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    title = models.CharField(max_length=255)
    script = models.TextField()
    metadata = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
