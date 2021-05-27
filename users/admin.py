from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import NewUser

"""
Customization class.
It's jsut some few customizations to the admin page
"""


class UserAdminSetup(UserAdmin):
    # Import the model
    model = NewUser

    # Define the fields to be displayed
    ordering = ('-start_date',)
    search_fields = ('email', 'user_name', 'first_name', 'last_name', 'phone_number') # Add search facility
    list_filter = ('user_name', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff')
    list_display = ('user_name', 'first_name', 'last_name', 'phone_number', 'email',)
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('user_name', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2',
    #                    'is_active', 'is_staff')}
    #      ),
    # )
    fieldsets = (
        ('Essential', {'fields': ('email', 'user_name', 'first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('user_name', 'password1', 'password2',)}),
        ('Essential', {'fields': ('email', 'first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )


# Add the NewUser to admin site
admin.site.register(NewUser, UserAdminSetup)
