from django.urls import path
from .views import *

urlpatterns = [
    path('', Index),
    path('p1', Page1),
    
]