from django.db import models
from profiles.models import Profile


class Tag(models.Model):
    TagName = models.CharField(max_length=100)
    Colour = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.TagName} - {self.Colour}"


class Post(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Title = models.CharField(max_length=100)
    Caption = models.TextField(blank=True)
    Image = models.ImageField(
        upload_to='images/', default='../default_post_e9srbd'
    )
    Tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True,
                            null=True)

    class Meta:
        ordering = ["-Created_at"]

    def __str__(self):
        return (f"{self.Title} by {self.Profile.User.username} " +
                f"at {self.Updated_at}")
