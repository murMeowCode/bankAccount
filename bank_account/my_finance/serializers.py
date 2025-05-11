from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import  User

        
class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone', 'username', 'first_name', 'last_name', 'email', 'password']


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # хеширование пароля
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # хеширование пароля при обновлении
        instance.save()
        return instance