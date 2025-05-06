from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from chat_room.models.chat_room import TradeChatRoom
from exchange_rate.models import ExchangeAgreement


@login_required
def fetch_new_messages_in_the_chatroom(request, agreement_id):
    last_message_id = int(request.GET.get('last_message_id', 0))
    agreement = get_object_or_404(ExchangeAgreement, pk=agreement_id)
    
    messages = TradeChatRoom.objects.filter(agreement=agreement, id__gt=last_message_id).order_by('timestamp')
    messages_data = [
        {
            'id': message.id,
            'content': message.content,
            'created': message.timestamp.strftime('%m/%d/%y %H:%M'),
            'user_name': message.user.get_full_name(),
            'user_image': message.user.profile_picture.url if message.user.profile_picture else '',
        } for message in messages
    ]
    return JsonResponse({'messages': messages_data})
