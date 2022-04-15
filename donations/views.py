from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
# Create your views here.


def myView(request):
    return HttpResponse('Hello World!')


class DonationListCreate(ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
