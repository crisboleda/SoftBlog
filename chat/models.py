from django.db import models
from django.http import Http404
from django.contrib.auth.models import User

# Create your models here.



class Group(models.Model):
        
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=80)
    members = models.ManyToManyField(User)
    picture = models.ImageField(upload_to='chat/groups')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def join_or_exit_group(self, user):
        if user in self.members.all():
            self.members.remove(user)
        else:
            self.members.add(user)
        self.save()



class Message(models.Model):
    content = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='message_of_group')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


from django.dispatch import receiver
from django.db.models.signals import pre_save

@receiver(pre_save, sender=Message)
def check_user_in_group(sender, instance, **kwargs):
    print(instance.author in instance.group.members.all())