from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from authen.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'email',  'is_active')
    ordering = ('phone_number',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number','email_verified')}),
    )
    
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'email_verified')}),
    )

    search_fields=('phone_number', 'email')
admin.site.register(User, CustomUserAdmin)
    