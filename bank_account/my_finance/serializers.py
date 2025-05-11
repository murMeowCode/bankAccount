from rest_framework.serializers import Serializer, ModelSerializer
from .models import UserProfile, User

class ProfileSerializer(ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['phone','username']