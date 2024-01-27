from rest_framework import serializers
from .models import  Apartment,City, Client

class ApartmentSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    clients = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = ['id', 'num_apartment', 'floor', 'square', 'date', 'price', 'status', 'location', 'clients']

    def get_location(self, obj):
        return obj.location.name if obj.location else None
    
    def get_clients(self, obj):
        return obj.clients.name if obj.clients else None
    


# class CitySerializerWithAppartments(serializers.ModelSerializer):
#     apartments = serializers.SerializerMethodField() 

#     class Meta:
#         model = City
#         fields = ['id', 'name', 'apartments']

#     def get_apartments(self, obj):
#         apartments = obj.apartment_set.all()
#         serializer = ApartmentSerializer(apartments, many=True)
#         return serializer.data
    
    
# class ClientSerializer(serializers.ModelSerializer):
#     apartments = serializers.SerializerMethodField()

#     class Meta:
#         model = Client
#         fields = ['id', 'name', 'number', 'deal', 'status', 'apartments']

#     def get_apartments(self, obj):
#         apartments = obj.apartment_set.all()
#         serializers = ApartmentSerializer(apartments, many=True) 
#         return serializers.data


