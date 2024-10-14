from django.db import models
from posts.models import Post
from profiles.models import Profile


class LikeDislike(models.Model):
    Post = models.ForeignKey(Post, related_name="likedislike",
                             on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile, related_name="LikingProfile",
                                on_delete=models.CASCADE)
    IsLike = models.BooleanField()
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        type = "Like" if self.IsLike else "Dislike"
        return f"{self.Post.Title} - {self.Profile.User.username} - {type}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["Post", "Profile"],
                                    name="UX_LikeDislike_Post_Profile")
        ]
