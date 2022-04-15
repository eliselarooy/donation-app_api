from django.db import models
from django.contrib.auth import get_user_model
from charities.models import Charity
User = get_user_model()

# Create your models here.


class SingleDonation(models.Model):
    user = models.ForeignKey(
        User, related_name='single_donations', on_delete=models.CASCADE)
    charity = models.ForeignKey(
        Charity, related_name='single_donations', on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"User: {self.user}, Amount: {self.total_amount}, Date: {self.date}"


class MonthlyDonation(models.Model):
    user = models.ForeignKey(
        User, related_name='monthly_donations', on_delete=models.CASCADE)
    charity = models.ForeignKey(
        Charity, related_name='monthly_donations', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
