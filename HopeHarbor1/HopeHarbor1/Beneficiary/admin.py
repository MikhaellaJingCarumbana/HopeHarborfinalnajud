from django.contrib import admin
from .models import Beneficiary, Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('house_number', 'street', 'barangay', 'city', 'state')
    search_fields = ('house_number', 'street', 'barangay', 'city', 'state')

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('Org', 'UserID', 'LastName', 'FirstName', 'Needs')
    list_filter = ('UserType', 'Needs', 'UserID', 'LastName', 'FirstName', 'Org')
    search_fields = ('FirstName', 'LastName', 'EmailAddress')
    filter_horizontal = ('AmountTrackerID', 'GoodsTrackerID')  # Use a list for filter_horizontal



# Register the models with their respective admin classes
admin.site.register(Address, AddressAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)
