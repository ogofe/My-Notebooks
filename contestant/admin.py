from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'user',
        'phone',
        'paid',
        'votes',
        'image',
        
    ]
    
    search_fields = [
        'user',
        'phone',
        'paid',
        'votes',       
    ]


admin.site.register(Account, AccountAdmin)
