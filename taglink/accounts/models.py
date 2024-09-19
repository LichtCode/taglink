from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    social_links = models.JSONField(default=dict, blank=True)

  # To reference the CustomUser model

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolios')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project_link = models.URLField(max_length=500, blank=True)
    project_images = models.JSONField(default=list, blank=True)  # Storing images as a JSON list of URLs
    portfolios = models.ManyToManyField(Portfolio, related_name='projects')  # Many-to-Many with Portfolio
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title