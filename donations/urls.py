from django.urls import path
from .views import *

urlpatterns = [
    path('single/', SingleDonationList.as_view()),
    path('single/create/', SingleDonationCreate.as_view()),
    path('single/<int:pk>/',
         SingleDonationRetrieveUpdateDelete.as_view()),
    path('monthly/', MonthlyDonationList.as_view()),
    path('monthly/create/', MonthlyDonationCreate.as_view()),
]
