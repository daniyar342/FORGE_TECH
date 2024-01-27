from django.shortcuts import render
from rest_framework import generics,status
from .serializers import ManagerRegisterSerializers
from rest_framework.response import Response


class ManagerRegisterView(generics.CreateAPIView):
    serializer_class = ManagerRegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Вы успешно зарегистрировались',status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)