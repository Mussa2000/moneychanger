from logging import info
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from accounts.models.user import CustomUser
from dashboard.helpers.province_stats import ProvinceStats
from django.db.models import Sum

from exchange_rate.forms import TransactionForm
from exchange_rate.models import ExchangeRate, Transaction
from exchange_rate.models import Currency


class DashboardListView(LoginRequiredMixin,TemplateView):   
    login_url = reverse_lazy('account_login')
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['exchange_rates'] = ExchangeRate.objects.all()
        context['transaction_form'] = TransactionForm()
        context['currencies'] = Currency.objects.all()

        return context
    


def get_exchange_rate(request):
    base_id = request.GET.get('base')
    target_id = request.GET.get('target')

    try:
        rate = ExchangeRate.objects.filter(
            base_currency_id=base_id,
            target_currency_id=target_id
        ).latest('date')

        return JsonResponse({
            'success': True,
            'rate': float(rate.rate),
            'base_code': rate.base_currency.code,
            'target_code': rate.target_currency.code,
            'rate_id': rate.id,
        })
    except ExchangeRate.DoesNotExist:
        return JsonResponse({'success': False})


from django.shortcuts import render, redirect
from django.contrib import messages

def create_transaction(request):
    if request.method == 'POST':
        base_currency_id = request.POST.get('base_currency')
        target_currency_id = request.POST.get('target_currency')
        amount = request.POST.get('amount')
        rate_id = request.POST.get('rate_id')
        transaction_type = request.POST.get('transaction_type')

        try:
            base_currency = Currency.objects.get(id=base_currency_id)
            target_currency = Currency.objects.get(id=target_currency_id)
            rate = ExchangeRate.objects.get(id=rate_id)
            amount_decimal = float(amount)
            received = amount_decimal * float(rate.rate)

            Transaction.objects.create(
                transaction_type=transaction_type,
                base_currency=base_currency,
                target_currency=target_currency,
                amount=amount_decimal,
                rate=rate,
                received_amount=received,
            )
            messages.success(request, "Transaction completed successfully.")
            return redirect('dashboard')  # or a success page
        except Exception as e:
            messages.error(request, f"Error processing transaction: {e}")

    # On GET or failed POST
    context = {
        'currencies': Currency.objects.all(),
    }
    return render(request, 'dashboard/dashboard.html', context)
