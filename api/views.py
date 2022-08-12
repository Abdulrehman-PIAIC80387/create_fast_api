from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializer import AddressSerial
from .models import Address

class AdressViewset(ModelViewSet):
    serializer_class = AddressSerial
    queryset = Address.objects.all()
