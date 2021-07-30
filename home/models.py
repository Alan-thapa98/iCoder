from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Contact(models.Model):
    name = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    content = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " by " + self.author
