from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=255, blank=True)

    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'