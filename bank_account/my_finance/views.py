from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import  UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from permissions import IsAdminOrOwner

class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminOrOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
