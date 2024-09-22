from django.db import models
from django.db.models.signals import post_save
from profiles.models import Profile

class Collections(models.Model):
    Profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    Views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Profile.Name}'s collection"


def create_collection(sender, instance, created, **kwargs):
    if created:
        Collections.objects.create(Profile=instance)

post_save.connect(create_collection, sender=Profile)