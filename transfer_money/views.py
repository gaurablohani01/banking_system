from django.shortcuts import render,redirect
from transfer_money.models import Account_Number, Balance, Transfer_Money
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction 


User = get_user_model()

@login_required(login_url="/login/")
def home(request):
    user_obj = User.objects.get(phone_number= request.user.phone_number)
    
    return render(request, 'index.html', {
    "user_details":user_obj
            })


@login_required(login_url="/login/")
def transfer_money(request):
    from_acc_obj = request.user.accnum.first()
    user_obj=User.objects.get(phone_number=request.user.phone_number)
    user_obj_acc=user_obj.accnum.all()
    first_acc = user_obj_acc.first()


    
    if request.method == "POST":
        to_acc_num = request.POST.get('to_acc')
        to_acc_name = request.POST.get('to_acc_name').lower()
        amount = int(request.POST.get('amount', 0))
        remarks = request.POST.get('remarks')
        
        to_acc_obj = Account_Number.objects.filter(acc_number=to_acc_num).first()
       
        

        if from_acc_obj and to_acc_obj:
            receiver_first_name = to_acc_obj.user.first_name.lower()
            receiver_last_name = to_acc_obj.user.last_name.lower()
            full_name = receiver_first_name + " " + receiver_last_name
            
            if full_name == to_acc_name:
             
                if amount > 0:
                    sender_balance_obj = Account_Number.objects.filter(user=request.user).first()
                    receiver_balance_obj = to_acc_obj
                    
                    if sender_balance_obj and receiver_balance_obj:
                        balance_sender = sender_balance_obj.accountnumber.availble_balance
                        if balance_sender >= amount:
                            with transaction.atomic():
                                sender_balance = sender_balance_obj.accountnumber
                                receiver_balance = receiver_balance_obj.accountnumber
                                print(sender_balance)
                                sender_balance.availble_balance = sender_balance.availble_balance - amount
                                receiver_balance.availble_balance += amount
                                sender_balance.save()
                                receiver_balance.save()

                                Transfer_Money.objects.create(
                                    from_acc=from_acc_obj,
                                    to_acc=to_acc_obj,
                                    amount=amount,
                                    remarks=remarks
                                )

                            messages.success(request, f'Transfer successful!')
                            return redirect('home')
                        else:
                            messages.warning(request, 'Insufficient balance.')
                    else:
                         messages.warning(request, 'Balance information not found.')
                else:
                    messages.warning(request, 'Amount must be greater than 0.')
            else:
                messages.warning(request, 'Account name and number do not match.')
        else:
            messages.warning(request, 'Account not found.')

            
    return render(request, 'transfermoney.html', {
       'balance': first_acc,
    })






