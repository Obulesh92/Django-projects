from django.db import models

# Create your models here.
class myblog(models.Model):
    post_title = models.CharField(max_length=200)
    your_name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    image_link = models.URLField(max_length=200, blank=True, null=True)
    Content = models.TextField()
    Tags = models.CharField(max_length=250, help_text='Comma-separated tags')

    def __str__(self):
        return (self.your_name+  '\t \t \t \t - \t \t \t \t' +self.post_title)
class contact(models.Model):
    your_name=models.CharField(max_length=100)
    your_email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return (self.your_name+  '\t \t \t \t - \t \t \t \t' +self.your_email)