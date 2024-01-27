from .models import Manager
from rest_framework.serializers import ModelSerializer


class ManagerRegisterSerializers(ModelSerializer):
    class Meta:
        model= Manager
        fields = ['email','password','username','number']

    def create(self, validated_data):
        user = Manager.objects.create_user(**validated_data)
        return user
    
class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id','email','username','number','created_at','amount_of_trade']