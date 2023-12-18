from django import forms
from .models import Beneficiary, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['house_number', 'street', 'barangay', 'city', 'state']

class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['Username', 'Password', 'FirstName', 'EmailAddress', 'LastName', 'Needs', 'Address', 'Org']

