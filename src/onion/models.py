from django.db import models


# Create your models here.

class Headline(models.Model):
    title = models.CharField(max_length=120)
    # image = models.ImageField()
    url = models.TextField()

    def __str__(self):
        return self.title
