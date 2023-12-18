from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('FeedbackID', 'TicketID', 'AdminID', 'AdminName', 'Contents')
    list_filter = ('AdminID__UserType',)  # Filter by Admin's UserType if needed
    search_fields = ('AdminName', 'Contents')

# Register the Feedback model with its admin class
admin.site.register(Feedback, FeedbackAdmin)
