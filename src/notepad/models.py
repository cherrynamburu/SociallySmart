from django.db import models

# Create your models here.

class Note(models.Model):
    text  = models.TextField(max_length=520)
    #image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.pk, self.text)

    def get_update_url(self):
        return "notes/{}/update".format(self.pk)

    def get_delete_url(self):
        return "notes/{}/delete".format(self.pk)
