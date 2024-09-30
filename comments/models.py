from django.db import models
from posts.models import Post
from profiles.models import Profile


class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Content = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Post.Title} - {self.Profile.Name} - {self.Content}"

    class Meta:
        ordering = ["-Created_at"]