from django.db import models
from django.contrib.auth.models import User

# Custom upload to for delete the old images
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.picture.delete()

    return 'users/pictures/' + filename


# User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profession = models.CharField(
        max_length=150, 
        null=True, 
        blank=True
    )
 
    picture = models.ImageField(
        upload_to=custom_upload_to, 
        null=True, 
        blank=True
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

