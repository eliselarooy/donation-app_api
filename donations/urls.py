from django.urls import path
from .views import *

urlpatterns = [
    path('donations/single/', SingleDonationListCreate.as_view()),
    path('donations/monthly/', MonthlyDonationListCreate.as_view()),
]
