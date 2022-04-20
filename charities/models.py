from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Charity(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    category = models.ManyToManyField(Category, related_name='charity', blank=True)

    def __str__(self):
      return self.name