from django.contrib import admin
from .models import SupportTicket

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('TicketID', 'AdminID', 'DonorID', 'Contents', 'ConfirmationType')
    list_filter = ('ConfirmationType',)
    search_fields = ('DonorID__FirstName', 'DonorID__LastName', 'Contents')

# Register the SupportTicket model with its admin class
admin.site.register(SupportTicket, SupportTicketAdmin)