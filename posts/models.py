from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    likes = models.IntegerField(blank=True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
