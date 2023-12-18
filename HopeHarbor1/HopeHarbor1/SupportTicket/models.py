from django.db import models
from AdminStaff.models import AdminStaff
from Donor.models import  Donor # Import the AdminStaff model


# Create your models here.
class SupportTicket(AdminStaff):
    TicketID = models.BigAutoField(primary_key=True)

    # Specify a related_name for the AdminID field to avoid clashes
    AdminID = models.ForeignKey(AdminStaff, on_delete=models.CASCADE, related_name='support_tickets')

    DonorID = models.ForeignKey(Donor, on_delete=models.CASCADE)
    Contents = models.CharField(max_length=500)

    CONFIRMATION_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
    )
    ConfirmationType = models.CharField(max_length=12, choices=CONFIRMATION_CHOICES)

    def __str__(self):
        return f"{self.DonorID} - {self.Contents}"
