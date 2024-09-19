from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=255, blank=True)
    image = CloudinaryField('image', default='https://res.cloudinary.com/dpjdwg51y/image/upload/v1726782033/k2wgf56y8stabvctolmu.png')
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
