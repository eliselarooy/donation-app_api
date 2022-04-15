from django.urls import path
from .views import *

urlpatterns = [
    path('charities/', CharityListCreate.as_view()),
]
