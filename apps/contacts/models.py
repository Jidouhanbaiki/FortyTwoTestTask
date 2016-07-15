from django.db import models


class Other(models.Model):
    left = models.CharField(max_length=48)
    right = models.CharField(max_length=48)

    def __unicode__(self):
        return self.left + ": " + self.right


class Contact(models.Model):
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)
    bio = models.CharField(max_length=512)
    jabber = models.CharField(max_length=48)
    skype = models.CharField(max_length=48)
    email = models.CharField(max_length=48)
    birthdate = models.DateField()
    other = models.ManyToManyField(Other)

    def __unicode__(self):
        return self.name + " " + self.surname
