from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Apartment,City,Client


class AllAppartmentsView(generics.ListAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all().select_related()


class DetailAppartmentView(generics.RetrieveAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all().select_related()
    lookup_field = "id"


class CreateApprtmentView(generics.CreateAPIView):
    serializer_class = ApartmentSerializer


class DeleteAppartmentView(generics.DestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class CityView(generics.ListAPIView):
    queryset = City.objects.all().select_related()
    serializer_class = CitySerializerWithAppartments



class ClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    