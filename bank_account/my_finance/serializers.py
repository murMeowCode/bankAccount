from rest_framework.serializers import Serializer, ModelSerializer
from .models import  User

        
class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['phone','username']