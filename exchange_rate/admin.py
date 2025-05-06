from django.contrib import admin
from .models import (
    Currency, ExchangeSource, ExchangeRate, Transaction,
    UserExchangeRate, ExchangeProposal, ChatMessage, ExchangeAgreement
)

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

@admin.register(UserExchangeRate)
class UserExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'target_currency', 'rate', 'user', 'date')
    list_filter = ('base_currency', 'target_currency', 'user', 'date')
    search_fields = ('base_currency__code', 'target_currency__code', 'user__username')
    ordering = ('-date',)

@admin.register(ExchangeProposal)
class ExchangeProposalAdmin(admin.ModelAdmin):
    list_display = ('seller_rate', 'buyer', 'proposed_rate', 'amount', 'status', 'created_at', 'responded_at')
    list_filter = ('status', 'created_at', 'responded_at')
    search_fields = ('seller_rate__user__username', 'buyer__username', 'status')
    ordering = ('-created_at',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('proposal', 'sender', 'message', 'timestamp')
    list_filter = ('proposal', 'sender', 'timestamp')
    search_fields = ('proposal__id', 'sender__username', 'message')
    ordering = ('-timestamp',)

@admin.register(ExchangeAgreement)
class ExchangeAgreementAdmin(admin.ModelAdmin):
    list_display = ('proposal', 'agreed_at', 'status')
    list_filter = ('status', 'agreed_at')
    search_fields = ('proposal__id', 'status')
    ordering = ('-agreed_at',)
