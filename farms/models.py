from django.contrib.gis.db import models
from django.conf import settings


class Farmer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Culture(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Plot(models.Model):
    contour = models.PolygonField()
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
