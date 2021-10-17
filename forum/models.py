from django.db import models
from django.db.models.base import Model

# Create your models here.

class Thread(models.Model):
    creator = models.CharField(max_length=30,null=False, blank=False, default="anonymous")
    title = models.CharField(max_length=200,null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['updated']

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True, blank=True)
    creator = models.CharField(max_length=30,null=False, blank=False, default="anonymous")
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

