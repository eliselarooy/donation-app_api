from rest_framework import serializers
from .models import *


class SingleDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleDonation
        fields = ('__all__')


class MonthlyDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyDonation
        fields = ('__all__')
