from django.db import models
from django.db.models.signals import post_save
from profiles.models import Profile
from brands.models import Series

class Collections(models.Model):
    Profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    Views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Profile.Name}'s collection"


class CollectionItem(models.Model):
    Collection = models.ForeignKey(Collections, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Series = models.ForeignKey(Series, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    Image = models.ImageField(
        upload_to='images/', default='../default_post_e9srbd'
    )

    constraints = [
        models.UniqueConstraint(fields=["Collection", "Name", "Series"], name="UX_CollectionItem_Coll_Name_Series")
    ]

    class Meta:
        ordering = [
            "Name","Series"
        ]

    def __str__(self):
        return f"{self.Name} - {self.Series} x{self.Quantity}"


def create_collection(sender, instance, created, **kwargs):
    if created:
        Collections.objects.create(Profile=instance)

post_save.connect(create_collection, sender=Profile)