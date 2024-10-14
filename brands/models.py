from django.db import models


class Brand(models.Model):
    BrandName = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["BrandName"]

    def __str__(self):
        return f"{self.BrandName}"


class Series(models.Model):
    SeriesName = models.CharField(max_length=100)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["SeriesName", "Brand"],
                                    name="UX_Series_SeriesName_Brand")
        ]

    def __str__(self):
        return f"{self.SeriesName} - {self.Brand}"
