from django.db import models
from User.models import User
from Donor.models import Amount_Tracker, Goods_Tracker

class Address(models.Model):
    house_number = models.CharField(max_length=50)
    street = models.CharField(max_length=50, default=' ')
    barangay = models.CharField(max_length=50, default=' ')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.house_number}, {self.street}, {self.barangay}, {self.city}, {self.state}"

class Beneficiary(User):
    NEEDS_CHOICES = (
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Shelter', 'Shelter'),
        ('Education', 'Education'),
        ('Medical', 'Medical'),
        ('Utilities', 'Utilities'),
        ('Transportation', 'Transportation'),
        ('Employment', 'Employment'),
        ('Other', 'Other'),
        # Add more charity needs options here
    )

    Needs = models.CharField(max_length=50, choices=NEEDS_CHOICES, default='food')
    Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    AmountTrackerID = models.ManyToManyField(Amount_Tracker, blank=True)
    GoodsTrackerID = models.ManyToManyField(Goods_Tracker, blank=True)  # Change to ManyToManyField
    UserType = models.CharField(
        max_length=12,
        choices=User.USER_TYPES,
        default='beneficiary',
    )
    Org = models.CharField(max_length=50, default='None')

    def __str__(self):
        return f"{self.Org} ({self.UserID}) - {self.LastName}, {self.FirstName}"
