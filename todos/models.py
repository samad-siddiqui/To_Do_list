from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    """A simple task management system"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.title
   
    