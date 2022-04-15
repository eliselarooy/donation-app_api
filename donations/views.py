from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
# Create your views here.


class DonationListCreate(ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
