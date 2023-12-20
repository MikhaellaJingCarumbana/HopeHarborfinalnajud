from django.forms import ModelForm
from django import forms
from .models import AdminStaff


class AdminStaffForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    usertype = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'User Type'}),
        initial='admin'
    )

    class Meta:
        model = AdminStaff
        fields = ['username', 'password', 'firstname', 'lastname', 'email', 'usertype']