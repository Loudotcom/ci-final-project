from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# Task model 

class Task (models.Model):

    options = (
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed")
    )
    
    name = models.CharField(max_length=100)
    notes = models.TextField()
    status = models.CharField(max_length=15, choices=options, default='pending')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name