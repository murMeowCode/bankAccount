from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .models import User, Transaction
from .serializers import  TransactionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrOwner

class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminOrOwner]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        # Фильтруем queryset в зависимости от прав пользователя
        queryset = User.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(id=self.request.user.id)
        return queryset
    
class TransactionAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)