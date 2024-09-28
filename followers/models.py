from django.db import models
from django.db.models import CheckConstraint, Q, F
from profiles.models import Profile


class Follower(models.Model):
    FollowingProfile = models.ForeignKey(
        Profile, related_name="OwningProfile", on_delete=models.CASCADE
    )
    FollowedProfile = models.ForeignKey(
        Profile, related_name="FollowedProfile", on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["FollowingProfile", "FollowedProfile"], name="UX_Follower_Following_Followed"),
            #https://medium.com/@ishakokutan/django-constraints-fa81d09cfa94
            models.CheckConstraint(check=~Q(FollowingProfile = F("FollowedProfile")), name='CK_Follower_Following_Followed')
        ]

    def __str__(self):
        return f"{self.FollowingProfile.User.username} following {self.FollowedProfile.User.username}"
