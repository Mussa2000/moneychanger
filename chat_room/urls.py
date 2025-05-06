from django.urls import path
from chat_room.views import (
    TradeChatRoomTemplateView,
    AgreementSendMessageView,
    
    fetch_new_messages_in_the_chatroom,
)
urlpatterns = [
    path('agreement/chat-room/<int:pk>/', TradeChatRoomTemplateView.as_view(), name="agreement-chat-room"),
    path('agreement/<int:pk>/chat-room/send-message/', AgreementSendMessageView.as_view(), name='send_message'),
    path('chat/<int:agreement_id>/fetch-new-messages/', fetch_new_messages_in_the_chatroom, name='fetch_new_messages'),
    
]
