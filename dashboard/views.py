from logging import info
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from accounts.models.user import CustomUser
from dashboard.helpers.province_stats import ProvinceStats
from django.db.models import Sum

from shield.models.alert import Alert
from shield.models.folder import Folder

class DashboardListView(LoginRequiredMixin,TemplateView):   
    login_url = reverse_lazy('account_login')
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        folders = Folder.objects.all()
        user_count = CustomUser.objects.all().count() or 0
        folder_count = Folder.objects.count() or 0
        alert_count = Alert.objects.count() or 0

        context['folders'] = folders
        context['user_count'] = user_count 
        context['folder_count'] = folder_count 
        context['alert_count'] = alert_count 

        return context
    
