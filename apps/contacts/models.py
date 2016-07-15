from django.db import models


class Other(models.Model):
    left = models.CharField(max_length=48)
    right = models.CharField(max_length=48)

    def __unicode__(self):
        return self.left + ": " + self.right


class Contact(models.Model):
    pass