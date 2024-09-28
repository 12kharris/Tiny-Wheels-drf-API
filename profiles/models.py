from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(
        upload_to='images/', default='../default_profile_cuucyn'
    )
    Name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-Created_at']

    def __str__(self):
        return f"{self.User}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(User=instance)


post_save.connect(create_profile, sender=User)
