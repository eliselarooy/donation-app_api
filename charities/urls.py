from django.urls import path
from .views import *

urlpatterns = [
    path('charities/', CharityListCreate.as_view()),
    path('charities/<int:pk>/', CharityDetail.as_view()),
]
