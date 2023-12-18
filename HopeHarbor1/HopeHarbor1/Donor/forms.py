from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Donor


class Donor_Login_Form(forms.ModelForm):
    Username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Password'}))

    class Meta:
        model = Donor
        fields = ['Username', 'Password']


class Donor_Registration_Form(forms.ModelForm):
    types = [
        ('cash', 'Cash'),
        ('materials', 'Materials'),
    ]
    EmailAddress = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'id': 'email'})
)
    Username = forms.CharField(required=True)
    Password = forms.PasswordInput()
    UserType = forms.CharField(widget=forms.HiddenInput, initial='donor')
    #DonationType = forms.ChoiceField(choices=types, widget=forms.Select(attrs={'id': 'select'}), label="Donation Type")
    FirstName = forms.CharField(
        label="First Name"
    )
    LastName = forms.CharField(
        label="Last Name"
    )

    class Meta:
        model = Donor
        fields = ['Username', 'EmailAddress', 'Password', 'FirstName', 'LastName', 'UserType']