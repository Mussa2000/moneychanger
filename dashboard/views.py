from logging import info
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from accounts.models.user import CustomUser
from dashboard.helpers.province_stats import ProvinceStats
from django.db.models import Sum

from exchange_rate.models import ExchangeRate


class DashboardListView(LoginRequiredMixin,TemplateView):   
    login_url = reverse_lazy('account_login')
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['exchange_rates'] = ExchangeRate.objects.all()

        return context
    
