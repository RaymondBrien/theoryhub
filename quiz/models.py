from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# class Quiz(models.Model):
#     """Stores a single quiz"""
#     title = models.CharField(max_length=200, unique=True)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     image = CloudinaryField('image', default='placeholder') 