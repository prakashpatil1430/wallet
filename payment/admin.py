from re import U
from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)

class WalletModelAdmin(admin.ModelAdmin):
    list_display = ['customer','id','owned_by','status','enabled_at','balance']


