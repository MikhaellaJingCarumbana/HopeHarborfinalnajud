from django.contrib import admin
from .models import AdminStaff

# Register your models here.
class AdminStaffAdmin(admin.ModelAdmin):
        list_display = ('UserID', 'FirstName', 'LastName', 'EmailAddress', 'UserType')
        search_fields = ('FirstName', 'LastName', 'EmailAddress')

admin.site.register(AdminStaff, AdminStaffAdmin)
