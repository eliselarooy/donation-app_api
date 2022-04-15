from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.


class SingleDonationList(ListAPIView):
    queryset = SingleDonation.objects.all()
    serializer_class = SingleDonationSerializer


class MonthlyDonationListCreate(ListCreateAPIView):
    queryset = MonthlyDonation.objects.all()
    serializer_class = MonthlyDonationSerializer


class SingleDonationCreate(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        request.data['user'] = request.user.id

        single_donation_serializer = SingleDonationSerializer(
            data=request.data)

        if single_donation_serializer.is_valid():
            single_donation_serializer.save()
            return Response(data=single_donation_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=single_donation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
