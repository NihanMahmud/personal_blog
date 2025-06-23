from django.db import models
from django.utils import timezone

# Create your models here.
class posts(models.Model):
    text=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
