from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)
    bio = models.TextField(default="")
    jabber = models.CharField(max_length=48, default="")
    skype = models.CharField(max_length=48, default="")
    email = models.CharField(max_length=48, default="")
    birthdate = models.DateField()
    other_contacts = models.TextField(default="")

    def __unicode__(self):
        return self.name + " " + self.surname
