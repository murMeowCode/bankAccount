from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction

@receiver(post_save, sender=Transaction)
def update_balance_on_transaction_save(sender, instance, created, **kwargs):
    """
    Обновляет баланс пользователя при создании или изменении транзакции
    """
    user = instance.user
    if created:
        # Для новой транзакции
        if instance.type == Transaction.INCOME:
            user.balance += instance.value
        else:
            user.balance -= instance.value
    
    user.save()

@receiver(post_delete, sender=Transaction)
def update_balance_on_transaction_delete(sender, instance, **kwargs):
    """
    Обновляет баланс пользователя при удалении транзакции
    """
    user = instance.user
    if instance.type == Transaction.INCOME:
        user.balance -= instance.value
    else:
        user.balance += instance.value
    user.save()