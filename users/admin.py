from django.contrib import admin
from .models import Marketer
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = Marketer
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'gender', 'percentage', 'Minimum_receive_money', 'reference_code', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'gender', 'percentage', 'Minimum_receive_money', 'reference_code', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'gender', 'percentage', 'receive_money', 'Minimum_receive_money', 'reference_code')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'gender', 'percentage', 'receive_money', 'Minimum_receive_money', 'reference_code', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Marketer, UserAdminConfig)
