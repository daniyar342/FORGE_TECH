from django.shortcuts import render
from rest_framework import generics
from .serializers import ApartmentSerializer,CitySerializerWithAppartments,ClientSerializer
from .models import Apartment,City,Client


class AppartmentView(generics.ListAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all().select_related()

class AppartmentDetailView(generics.RetrieveAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all().select_related()

    lookup_field = "id"


class CityView(generics.ListAPIView):
    queryset = City.objects.all().select_related()
    serializer_class = CitySerializerWithAppartments



class ClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    