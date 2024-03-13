from logging import info
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class DashboardListView(LoginRequiredMixin,TemplateView):   
    login_url = reverse_lazy('account_login')
    template_name = 'dashboard/dashboard.html'
    
