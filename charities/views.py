from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from charities.models import Charity
from charities.serializers import *

# Create your views here.


class CharityListCreate(ListCreateAPIView):
    queryset = Charity.objects.all()
    serializer_class = PopulatedCharitySerializer


class CharityDetail(RetrieveAPIView): 
    queryset = Charity.objects.all()
    serializer_class = PopulatedCharitySerializer