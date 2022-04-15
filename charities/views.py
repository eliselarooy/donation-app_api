from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from charities.models import Charity
from charities.serializers import CharitySerializer

# Create your views here.


class CharityListCreate(ListCreateAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer
