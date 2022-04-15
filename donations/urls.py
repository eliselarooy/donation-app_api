from django.urls import path
from .views import *

urlpatterns = [
    path('donations/', DonationListCreate.as_view()),
]
