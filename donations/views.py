from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
# Create your views here.


class SingleDonationListCreate(ListCreateAPIView):
    queryset = SingleDonation.objects.all()
    serializer_class = SingleDonationSerializer


class MonthlyDonationListCreate(ListCreateAPIView):
    queryset = MonthlyDonation.objects.all()
    serializer_class = MonthlyDonationSerializer
