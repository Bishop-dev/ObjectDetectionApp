from django.db import models


class Person(models.Model):
    instagram = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
