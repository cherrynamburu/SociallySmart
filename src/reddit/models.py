from django.db import models

# Create your models here.

class Story(models.Model):
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=2000, null=True, blank=True)
    comments = models.IntegerField(default=0)

    def build_url(self):
        self.url = '{0}{1}'.format('https://www.reddit.com/', self.code)
        return self.url

    def __str__(self):
        return self.title
