from django.db import models
from profiles.models import Profile


class Follower(models.Model):
    FollowingProfile = models.ForeignKey(
        Profile, related_name="owning_profile", on_delete=models.CASCADE
    )
    FollowedProfile = models.ForeignKey(
        Profile, related_name="followed_profile", on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["FollowingProfile", "FollowedProfile"], name="UX_Follower_Follower_Followed")
        ]

    def __str__(self):
        return f"{self.FollowingProfile.User.username} following {self.FollowedProfile.User.username}"
