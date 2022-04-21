from rest_framework import serializers
from .models import Category, Charity


class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class PopulatedCharitySerializer(CharitySerializer):
    category = CategorySerializer(many=True)