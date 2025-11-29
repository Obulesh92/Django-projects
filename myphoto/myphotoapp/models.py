from django.db import models
# Create your models here.
class MyPhoto(models.Model):
    title = models.CharField(max_length=200) # optional title
    image = models.ImageField(upload_to='my_images/')        # saves to media/my_images/
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title or f"Photo {self.id}"  # fallback if title is blank
    
from django.db import models

class MyVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    def __str__(self):
        return self.title
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.subject}"
