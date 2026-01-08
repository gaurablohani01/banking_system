from django.db import models
from django.conf import settings

class Account_Number(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="accnum")
    acc_number = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.user} Account Number'

class Balance(models.Model):
    acc_num = models.OneToOneField(Account_Number, related_name='accountnumber', on_delete=models.CASCADE)
    availble_balance = models.IntegerField(default=0,)
    
    def __str__(self):
        return f'{self.acc_num} balance'

class Transfer_Money(models.Model):
    from_acc = models.ForeignKey(Account_Number, on_delete=models.CASCADE, related_name="sent_trans")
    to_acc = models.ForeignKey(Account_Number, on_delete=models.CASCADE, related_name="receive_trans")
    amount = models.IntegerField()
    remarks= models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_acc} to {self.to_acc} transfer money'
