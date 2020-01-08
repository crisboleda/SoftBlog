from django.db import models
from django.contrib.auth.models import User

# App posts
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    description = models.TextField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
