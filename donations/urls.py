from django.urls import path
from .views import *

urlpatterns = [
    path('single/', SingleDonationList.as_view()),
    path('single/create', SingleDonationCreate.as_view()),
    path('monthly/', MonthlyDonationListCreate.as_view()),
]
