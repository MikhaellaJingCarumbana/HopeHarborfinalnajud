from django.db import models
from SupportTicket.models import SupportTicket
from AdminStaff.models import AdminStaff


# Create your models here.
class Feedback(models.Model):
    FeedbackID = models.BigAutoField(primary_key=True)

    # Specify related_name for TicketID field
    TicketID = models.ForeignKey(
        SupportTicket,
        on_delete=models.CASCADE,
        related_name='DonorTicket'  # Custom related_name
    )

    # Specify related_name for AdminID field
    AdminID = models.ForeignKey(
        AdminStaff,
        on_delete=models.CASCADE,
        related_name='Adminfeedbacks'  # Custom related_name
    )

    AdminName = models.CharField(max_length=50)
    Contents = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.TicketID} - {self.AdminName}"
