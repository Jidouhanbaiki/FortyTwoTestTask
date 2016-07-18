from django.db import models
import time


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


class RequestLog(models.Model):
    method = models.CharField(max_length=32)
    path = models.CharField(max_length=32)
    remote_addr = models.CharField(max_length=32)
    http_user_agent = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    time = models.FloatField()

    def __str__(self):
        return "{0} {1} {2} {3}".format(
            self.username,
            self.method,
            self.http_user_agent,
            time.ctime(self.time)
        )
