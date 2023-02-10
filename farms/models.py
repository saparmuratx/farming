from django.db import models


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
