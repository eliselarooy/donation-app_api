from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    image = models.CharField(max_length=200, null=True)
    goal_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)