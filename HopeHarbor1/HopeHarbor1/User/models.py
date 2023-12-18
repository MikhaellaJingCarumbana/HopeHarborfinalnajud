from django.db import models


class User(models.Model):
    UserID = models.BigAutoField(primary_key=True)
    Username = models.CharField(max_length=30, default="", unique=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    EmailAddress = models.EmailField()
    USER_TYPES = [
        ('donor', 'Donor'),
        ('beneficiary', 'Beneficiary'),
        ('admin', 'Admin'),
    ]
    UserType = models.CharField(max_length=12, choices=USER_TYPES)
    Password = models.CharField(max_length=128)  # Store the hashed password

    class Meta:
        abstract = True
