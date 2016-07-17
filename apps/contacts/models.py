from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)
    bio = models.TextField()
    jabber = models.CharField(max_length=48)
    skype = models.CharField(max_length=48)
    email = models.CharField(max_length=48)
    birthdate = models.DateField()
    other_contacts = models.TextField()

    def __unicode__(self):
        return self.name + " " + self.surname
