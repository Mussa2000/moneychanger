from django.contrib import admin
from .models import TradeChatRoom

# Register your models here.
@admin.register(TradeChatRoom)
class TradeChatRoomAdmin(admin.ModelAdmin):
    list_display = ('agreement', 'user', 'timestamp')
    search_fields = ('user__username', 'content')
    list_filter = ('timestamp',)