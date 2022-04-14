from django.db import models

# Create your models here.


class Charity(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, blank=True)
