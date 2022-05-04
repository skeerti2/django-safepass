import imp
from django import forms
from .models import Account

class NewAccountDetailsForm(forms.ModelForm):
    account_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['account_domain','account_username', 'account_password']