from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(max_length=15000, blank=False, null=False)
    author = models.ForeignKey(User, models.CASCADE)
    blog_pic = models.ImageField(upload_to='blog_pics/', default='blog_pics/default.jpg')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}\'s article"
    

    def save(self, *args, **kwargs):
        return super(Blog, self).save(*args, **kwargs)