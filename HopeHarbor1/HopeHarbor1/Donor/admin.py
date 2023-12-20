from django.contrib import admin
from .models import Donor, CashDetails, GoodsDetails, Currency, DIK, Amount_Tracker, Goods_Tracker
from django.contrib import admin
from django.db.models import DecimalField
from django.core.exceptions import ValidationError



class DonorAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'FirstName', 'LastName', 'EmailAddress', 'UserType', 'DonationType', 'Username', 'Password')
    list_filter = ('UserType', 'DonationType')
    search_fields = ('FirstName', 'LastName', 'EmailAddress')
    # Add other customization options as needed

class CashDetailsAdmin(admin.ModelAdmin):
    list_display = ('CashID', 'DonorID', 'Amount', 'Date')
    list_filter = ('DonorID__UserType',)  # Filter by Donor's UserType
    search_fields = ('DonorID__FirstName', 'DonorID__LastName')

class GoodsDetailsAdmin(admin.ModelAdmin):
    list_display = ('GDID', 'DonorID', 'DateofDonation')
    list_filter = ('DonorID__UserType',)  # Filter by Donor's UserType
    search_fields = ('DonorID__FirstName', 'DonorID__LastName')



class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('CurrencyID', 'CashID', 'CurrencyType')

class DIKAdmin(admin.ModelAdmin):
    list_display = ('DikID', 'GDID', 'DikType')

class Amount_TrackerAdmin(admin.ModelAdmin):
    list_display = ('Amount_TrackerID', 'CurrencyID', 'AdminID', 'Amount')

class Goods_TrackerAdmin(admin.ModelAdmin):
    list_display = ('GoodsTrackerID', 'DonationInKind', 'AdminID', 'Quantity')

# Register the models with their respective admin classes
admin.site.register(Donor, DonorAdmin)
admin.site.register(CashDetails, CashDetailsAdmin)
admin.site.register(GoodsDetails, GoodsDetailsAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(DIK, DIKAdmin)
admin.site.register(Amount_Tracker, Amount_TrackerAdmin)
admin.site.register(Goods_Tracker, Goods_TrackerAdmin)
