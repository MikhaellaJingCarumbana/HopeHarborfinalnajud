from django.db import models
from User.models import User
from Donor.models import Amount_Tracker, Goods_Tracker
from django.forms import forms


class Address(models.Model):
    house_number = models.CharField(max_length=50)
    street = models.CharField(max_length=50, default= ' ')
    barangay = models.CharField(max_length=50, default=' ')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.house_number}, {self.street}, {self.barangay}, {self.city}, {self.state}"


class Beneficiary(User):
    NEEDS_CHOICES = (
        ('food', 'Food'),
        ('clothing', 'Clothing'),
        ('shelter', 'Shelter'),
        ('education', 'Education'),
        ('medical', 'Medical'),
        ('utilities', 'Utilities'),
        ('transportation', 'Transportation'),
        ('employment', 'Employment'),
        ('other', 'Other'),
        # Add more charity needs options here
    )

    Needs = models.CharField(max_length=50, choices=NEEDS_CHOICES, default='food')
    Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    AmountTrackerID = models.ForeignKey(Amount_Tracker, on_delete=models.CASCADE,blank= True, null=True)
    GoodsTrackerID = models.ForeignKey(Goods_Tracker, on_delete=models.CASCADE, blank= True, null=True)
    UserType = models.CharField(
        max_length=12,
        choices=User.USER_TYPES,  # Use choices from User model
        default='beneficiary',  # Set the default to 'beneficiary'
    )
    Org = models.CharField(max_length=50, default='None')

    def __str__(self):
        return f"{self.Org} ({self.UserID}) - {self.LastName}, {self.FirstName} "
