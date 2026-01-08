import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Account_Number, Balance

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_banking_info(sender, instance, created, **kwargs):
    if created:
        random_acc = random.randint(1000000000, 9999999999)
        
        new_account = Account_Number.objects.create(
            user=instance, 
            acc_number=random_acc
        )
        
        Balance.objects.create(
            acc_num=new_account, 
            availble_balance=0
        )