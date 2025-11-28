from django.db import models

# Create your models here.
class Todo_data(models.Model):
    task = models.CharField(max_length=255)
    def __str__(self):
        return  self.task