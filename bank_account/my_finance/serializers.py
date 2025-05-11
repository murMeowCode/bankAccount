from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Transaction

        
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
     
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('user', 'date')

    def validate(self, data):
        """
        Проверяем, что у пользователя достаточно средств для расходной операции
        """
        if data.get('type') == Transaction.OUTCOME:
            user = self.context['request'].user
            if user.balance < data.get('value', 0):
                raise serializers.ValidationError(
                    "Недостаточно средств на балансе для этой операции"
                )
        return data
