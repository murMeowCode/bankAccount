from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Указываем уникальные related_name для избежания конфликтов
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="finance_user_groups",
        related_query_name="finance_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="finance_user_permissions",
        related_query_name="finance_user",
    )
    
    phone = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        # Указываем, что это новая модель пользователя
        swappable = 'AUTH_USER_MODEL'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    currency = models.CharField(max_length=3, default='RUB')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Transaction(models.Model):
    INCOME = 'income'
    OUTCOME = 'outcome'
    TYPE_CHOICES = [
        (INCOME, 'Доход'),
        (OUTCOME, 'Расход'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Добавил связь с пользователем
    value = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # Добавил поле типа транзакции
    
    def __str__(self):
        return f"{self.get_type_display()}: {self.value} ({self.category.name})"