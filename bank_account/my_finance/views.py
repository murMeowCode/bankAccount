from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import UserProfile, User
from .serializers import ProfileSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'  # это поле по умолчанию, можно не указывать
    
class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
