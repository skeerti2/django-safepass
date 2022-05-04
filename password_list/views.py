from inspect import ismethoddescriptor
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account, User
from .forms import NewAccountDetailsForm

# Create your views here.
def postLoginLanding(request):
    current_user = request.user
    print(current_user)
    user = User.objects.get(username=current_user)
    if request.method=="POST":
        form = NewAccountDetailsForm(data=request.POST)
        if form.is_valid():
            form_account_username = form['account_username'].value()
            form_account_password = form['account_password'].value()
            form_account_domain = form['account_domain'].value()
            account_obj = Account(account_username=form_account_username, account_password= form_account_password,
            account_domain=form_account_domain, username=user)
            print(account_obj)
            account_obj.save()
            #account = form.save()
            #print(account)
            return redirect(reverse('password_list:postLoginLanding'))
    else:
        user_accounts = Account.objects.filter(username=user)
        # print(user_accounts)
        return render(request, "accounts.html", {'accounts_data': user_accounts})

def displaycreateAccountForm(request):
    print("came here")
    if request.method=="GET":
        form = NewAccountDetailsForm()
        return render(request, "createAccount.html", {'account_details_form': form})
    
def retrievePassword(request):
    if request.method=="POST":
        account_id = request.POST.account_id
        account = Account.objects.get(id=account_id)
        #decrypt below and send        
        account_details = {'account_domain':account.account_domain, 'account_username': account.account_username,
        'account_password': account.account_username}
        return render(request, "showPassword.html", {'account_details': account_details})