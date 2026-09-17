from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
