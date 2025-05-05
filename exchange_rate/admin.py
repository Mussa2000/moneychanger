from django.contrib import admin
from .models import Currency, ExchangeSource, ExchangeRate, Transaction

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    ordering = ('name',)

@admin.register(ExchangeSource)
class ExchangeSourceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'base_currency', 'target_currency', 'rate', 'source')
    list_filter = ('date', 'base_currency', 'target_currency', 'source')
    search_fields = ('base_currency__code', 'target_currency__code', 'source__name')
    ordering = ('-date',)
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'base_currency', 'target_currency', 'amount', 'rate', 'received_amount', 'created_at')
    list_filter = ('transaction_type', 'base_currency', 'target_currency', 'created_at')
    search_fields = ('base_currency__code', 'target_currency__code', 'transaction_type')
    ordering = ('-created_at',)
