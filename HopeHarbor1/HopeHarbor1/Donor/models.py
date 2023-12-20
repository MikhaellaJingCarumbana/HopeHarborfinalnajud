from django.db import models
from User.models import User
from AdminStaff.models import AdminStaff
from django.core.validators import MinValueValidator


class Donor(User):
    DONATION_CHOICES = (
        ('cash', 'Cash'),
        ('materials', 'Materials'),
    )
    DonationType = models.CharField(max_length=10, choices=DONATION_CHOICES)
    UserType = models.CharField(
        max_length=12,
        choices=User.USER_TYPES,  # Use choices from User model
        default='donor',  # Set the default to 'donor'
    )




class CashDetails(models.Model):
    CashID = models.BigAutoField(primary_key = True)
    DonorID = models.ForeignKey(Donor, on_delete=models.CASCADE)
    Amount = models.FloatField(default=1.0, validators=[MinValueValidator(1.0)])
    Date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.DonorID} - {self.Date}"




class GoodsDetails(models.Model):
    GDID = models.BigAutoField(primary_key = True)
    DonorID = models.ForeignKey(Donor, on_delete=models.CASCADE)
    DateofDonation = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.DateofDonation}"


class Currency(models.Model):
    CurrencyID = models.BigAutoField(primary_key=True)
    CashID = models.ForeignKey(CashDetails, on_delete=models.CASCADE)
    CURRENCY_CHOICES = (
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('JPY', 'Japanese Yen'),
        ('GBP', 'British Pound Sterling'),
        ('CAD', 'Canadian Dollar'),
        ('AUD', 'Australian Dollar'),
        ('CHF', 'Swiss Franc'),
        ('CNY', 'Chinese Yuan'),
        ('INR', 'Indian Rupee'),
        ('RUB', 'Russian Ruble'),
        ('ZAR', 'South African Rand'),
        ('AED', 'United Arab Emirates Dirham'),
        ('SGD', 'Singapore Dollar'),
        ('NZD', 'New Zealand Dollar'),
        ('HKD', 'Hong Kong Dollar'),
        ('SEK', 'Swedish Krona'),
        ('NOK', 'Norwegian Krone'),
        ('DKK', 'Danish Krone'),
        ('KRW', 'South Korean Won'),
        ('BRL', 'Brazilian Real'),
        ('MXN', 'Mexican Peso'),
        ('ARS', 'Argentine Peso'),
        ('TRY', 'Turkish Lira'),
        ('EGP', 'Egyptian Pound'),
        ('PHP', 'Philippine Peso'),
        # Add more currencies as needed
    )
    CurrencyType = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='PHP')

    def __str__(self):
        return self.get_CurrencyType_display()


class DIK(models.Model):
    DikID = models.BigAutoField(primary_key=True)
    GDID = models.ForeignKey(GoodsDetails, on_delete=models.CASCADE)

    # Use the same tuple of choices as in the Beneficiary model
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

    DikType = models.CharField(max_length=50, choices=NEEDS_CHOICES, default='food')

    def __str__(self):
        return f"Date of Donation: {self.GDID} - Type: {self.DikType}"


class Amount_Tracker(models.Model):
    Amount_TrackerID = models.BigAutoField(primary_key = True)
    CurrencyID = models.ForeignKey(Currency, on_delete=models.CASCADE)
    AdminID = models.ForeignKey(AdminStaff, on_delete=models.CASCADE)
    Amount = models.FloatField(default=1.0, validators=[MinValueValidator(1)])



class Goods_Tracker(models.Model):
    GoodsTrackerID = models.BigAutoField(primary_key = True)
    DonationInKind = models.ForeignKey(DIK, on_delete=models.CASCADE)
    AdminID = models.ForeignKey(AdminStaff, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0, validators=[MinValueValidator(1)])


# Rowen and Gian