from django.contrib import admin
from transfer_money.models import Account_Number, Balance,Transfer_Money

# Register your models here.
admin.site.register(Account_Number)
admin.site.register(Balance)
admin.site.register(Transfer_Money)

