from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin
class AccountAdmin(UserAdmin):
    fields = ('email', 'username','avatar', 'password', 'is_admin','is_staff', 'is_superuser')
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_staff','is_superuser')
    readonly_fields = ('id', 'date_joined')
    searh_fields = ('email','username')

    fieldsets = ()         
    filter_horizontal = ()
    list_filter = ()
admin.site.register(Account, AccountAdmin)
