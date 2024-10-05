from django.db import models


class Kittens(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    description = models.TextField(max_length=100)
    breed = models.CharField(max_length=50)
