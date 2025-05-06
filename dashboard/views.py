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
from exchange_rate.models import ExchangeAgreement, ExchangeProposal, ExchangeRate, Transaction, UserExchangeRate
from exchange_rate.models import Currency


class DashboardListView(LoginRequiredMixin,TemplateView):   
    login_url = reverse_lazy('account_login')
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['exchange_rates'] = ExchangeRate.objects.all()
        context['transaction_form'] = TransactionForm()
        context['exchange_proposal_form'] = ExchangeProposalForm()
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
from exchange_rate.forms import ExchangeProposalForm

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


def create_exchange_proposal(request):
    if request.method == 'POST':
        base_currency_id = request.POST.get('base_currency')
        target_currency_id = request.POST.get('target_currency')
        amount = request.POST.get('amount')
        seller_rate_id = request.POST.get('seller_rate')
        proposed_rate = request.POST.get('proposed_rate')

        try:
            # Ensure the currencies exist
            base_currency = Currency.objects.get(id=base_currency_id)
            target_currency = Currency.objects.get(id=target_currency_id)

            # Ensure the seller rate exists
            seller_rate = UserExchangeRate.objects.get(id=seller_rate_id)

            # Validate amount and proposed rate
            amount_decimal = float(amount)
            if amount_decimal <= 0:
                raise ValueError("Amount must be greater than zero.")
            if proposed_rate and float(proposed_rate) <= 0:
                raise ValueError("Proposed rate must be greater than zero.")

            # Create the ExchangeProposal
            exchange_proposal = ExchangeProposal.objects.create(
                seller_rate=seller_rate,
                buyer=request.user,  # Assuming the current user is the buyer
                proposed_rate=proposed_rate,
                amount=amount_decimal,
            )

            # Create the ExchangeAgreement (status will be Pending by default)
            exchange_agreement = ExchangeAgreement.objects.create(
                proposal=exchange_proposal,
                status='Pending',
            )

            messages.success(request, "Your proposal has been submitted successfully.")
            return redirect('dashboard')  # or another success page

        except Currency.DoesNotExist:
            messages.error(request, "Invalid currencies selected.")
        except UserExchangeRate.DoesNotExist:
            messages.error(request, "Invalid seller rate selected.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Error creating proposal: {e}")

    else:
        print("GET request received for creating exchange proposal encountered an error")

    context = {
        'currencies': Currency.objects.all(),
    }

    return render(request, 'dashboard/dashboard.html', context)

# serializers.py

def get_seller_rates(request):
    base_id = request.GET.get('base')
    target_id = request.GET.get('target')

    if not base_id or not target_id or base_id == target_id:
        return JsonResponse({'success': False, 'error': 'Invalid currency selection'})

    seller_rates = UserExchangeRate.objects.filter(
        base_currency_id=base_id,
        target_currency_id=target_id
    ).select_related('user').order_by('-rate')

    data = [
        {
            'id': rate.id,
            'rate': float(rate.rate),
            'user_name': rate.user.username if rate.user else 'Unknown',
        }
        for rate in seller_rates
    ]

    return JsonResponse({'success': True, 'rates': data})


# views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def accept_proposal_view(request, pk):
    agreement = get_object_or_404(ExchangeAgreement, pk=pk)

    if request.method == 'POST':
        if agreement.status != 'Pending':
            messages.error(request, 'This agreement has already been processed.')
            return redirect('dashboard')

        # Mark proposal as accepted
        agreement.status = 'Accepted'
        agreement.responded_at = timezone.now()
        agreement.save()

        messages.success(request, 'agreement accepted successfully.')
        return redirect('proposal-index')

    messages.success(request, 'An error occured.')
    return redirect('proposal-index')


@login_required
def reject_proposal_view(request, pk):
    agreement = get_object_or_404(ExchangeAgreement, pk=pk)

    if request.method == 'POST':
        if agreement.status != 'Pending':
            messages.error(request, 'This agreement has already been processed.')
            return redirect('dashboard')

        # Mark proposal as rejected
        agreement.status = 'Rejected'
        agreement.responded_at = timezone.now()
        agreement.save()


        messages.success(request, 'agreement rejected successfully.')
        return redirect('proposal-index')

    messages.success(request, 'An error occured.')
    return redirect('proposal-index')