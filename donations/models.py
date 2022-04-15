from django.db import models
from django.contrib.auth import get_user_model
from charities.models import Charity
User = get_user_model()

# Create your models here.


class Donation(models.Model):
    Once = 'O'
    Monthly = 'M'
    options = [
        (Once, 'Once'),
        (Monthly, 'Monthly')
    ]

    user = models.ForeignKey(
        User, related_name='donations', on_delete=models.CASCADE)
    charity = models.ForeignKey(
        Charity, related_name='donations', on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    frequency = models.CharField(
        choices=options, default=Once, max_length=10)

    def __str__(self):
        return f"User: {self.user}, Amount: {self.total_amount}, Date: {self.date}"
