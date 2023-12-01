from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    author = models.CharField()
    publised_date = models.DateField()

