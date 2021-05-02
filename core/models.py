from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
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
        super(Blog, self).save(*args, **kwargs)
        if self.blog_pic:
            img = Image.open(self.blog_pic.path, 'r')
            if img.height > 300 or img.width > 300:
                img.thumbnail((300,300))
                img.save(self.blog_pic.path)


class Comment(models.Model):
    content = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username}\' comment'


class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    date_of_action = models.DateTimeField(auto_now_add=True)


    class Meta:
        constraints  = [
            models.UniqueConstraint(fields=['user','following_user'],  name="unique_followers")
        ]
        ordering = ('-date_of_action', )
    def __str__(self):
        return f'{self.user} is following {self.following_user}'
    
