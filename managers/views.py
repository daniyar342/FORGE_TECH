from django.shortcuts import render
from rest_framework import generics,status
from .serializers import *
from rest_framework.response import Response
from .models import Manager

class ManagerRegisterView(generics.CreateAPIView):
    serializer_class = ManagerRegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Вы успешно зарегистрировались',status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        

class DeleteManagerView(generics.DestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerRegisterSerializers
    lookup_field = 'id'


class AllManagersView(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class UpdateManagerView(generics.UpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    lookup_field = 'id'