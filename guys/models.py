from __future__ import unicode_literals

from django.db import models

class Guy(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=2)
    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return "/guys/%i/" % self.id
