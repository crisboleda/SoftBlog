from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Caterory(models.Model):

    name_category = models.CharField(
        unique=True,
        max_length=30
    )

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name_category)

class Tag(models.Model):
    name_tag = models.CharField(max_length=20, unique=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name_tag)


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    data_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_actived = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    tags = models.ManyToManyField(Tag, related_name='tags_posts')
    category = models.ForeignKey(Caterory, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return "{}".format(self.title)

