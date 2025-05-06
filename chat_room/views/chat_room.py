from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.db.models import F
import logging
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from chat_room.models.chat_room import TradeChatRoom
from exchange_rate.models import ExchangeAgreement

logger = logging.getLogger(__name__)
from django.http import JsonResponse
from django.views import View

from django.views.generic import TemplateView

class TradeChatRoomTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "chat_room/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agreement = get_object_or_404(ExchangeAgreement, pk=self.kwargs['pk'])
        messages = TradeChatRoom.objects.filter(agreement=agreement).order_by('timestamp')
        last_message_id = messages.last().id if messages.exists() else 0  # Safely get last message ID
        
        context['agreement'] = agreement
        context['messages'] = messages
        context['last_message_id'] = last_message_id
        return context


class AgreementSendMessageView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        agreement = get_object_or_404(ExchangeAgreement, pk=self.kwargs['pk']) 
        content = request.POST.get('content') 
        
        # Check if content is empty
        if not content:
            return JsonResponse({'success': False, 'error': 'Message content cannot be empty'}, status=400)

        message = TradeChatRoom.objects.create(agreement=agreement, user=request.user, content=content)


        return JsonResponse({
            'success': True,
            'message': {
                'content': message.content,
                'created_at': message.timestamp.strftime('%B %d, %Y, %I:%M %p'),
                'user': {
                    'username': request.user.username,
                    'profile_picture_url': request.user.profile_picture.url if request.user.profile_picture else ''
                }
            }
        })
