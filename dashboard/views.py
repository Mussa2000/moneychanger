from logging import info
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from accounts.models.user import CustomUser
from dashboard.helpers.province_stats import ProvinceStats
from receivables.models.bank import Bank
from receivables.models.payment import Payment
from receivables.models.province import Province
from receivables.models.transaction import Transaction
from django.db.models import Sum

class DashboardListView(LoginRequiredMixin,TemplateView):   
    login_url = reverse_lazy('account_login')
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        farmers_count = CustomUser.objects.filter(is_farmer=True).count() or 0
        bank_count = Bank.objects.count() or 0
        province_count = Province.objects.count() or 0
        paid_amount = Transaction.objects.filter(status='paid').aggregate(total_paid_amount=Sum('amount_paid'))['total_paid_amount'] or 0.00
        partially_paid_amount= Transaction.objects.filter(status='pending', amount_paid__gt=0).aggregate(total_partially_paid_amount=Sum('amount_paid'))['total_partially_paid_amount'] or 0.00
        province_stats = ProvinceStats.get_stats()
        
        #is farmer stats
        farmer_paid_amount = Transaction.objects.filter(user=user, status='paid').aggregate(total_paid_amount=Sum('amount_paid'))['total_paid_amount'] or 0.00
        farmer_partially_paid_amount = Transaction.objects.filter(user=user, status='pending', amount_paid__gt=0).aggregate(total_partially_paid_amount=Sum('amount_paid'))['total_partially_paid_amount'] or 0.00
        farmer_invoice_count = Transaction.objects.filter(user=user).count()

        if user.is_farmer:
            transactions = Transaction.objects.filter(user=user)
        else:
            transactions = Transaction.objects.all()
        
        context['transactions'] = transactions
        context['farmers_count'] = farmers_count
        context['bank_count'] = bank_count 
        context['paid_amount'] = paid_amount 
        context['partially_paid_amount'] = partially_paid_amount 
        context['province_count'] = province_count
        context['province_stats'] =  province_stats
        
        context['farmer_paid_amount'] = farmer_paid_amount 
        context['farmer_partially_paid_amount'] = farmer_partially_paid_amount
        context['farmer_invoice_count'] = farmer_invoice_count 
        return context
    
