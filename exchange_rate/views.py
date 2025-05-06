from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, View
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Currency, ExchangeAgreement, ExchangeProposal, ExchangeSource, ExchangeRate, Transaction, UserExchangeRate
from .forms import CurrencyForm, ExchangeSourceForm, ExchangeRateForm, UserExchangeRateForm

# ------------------ Currency ------------------

class CurrencyListView(ListView):
    model = Currency
    context_object_name = "currencies"
    template_name = "currency/index.html"


class CurrencyCreateView(SuccessMessageMixin, CreateView):
    model = Currency
    form_class = CurrencyForm
    template_name = "currency/create.html"
    success_message = "Currency created successfully"

    def get_success_url(self):
        return reverse("currency-index")


class CurrencyUpdateView(SuccessMessageMixin, UpdateView):
    model = Currency
    form_class = CurrencyForm
    template_name = "currency/update.html"
    success_message = "Currency updated successfully"

    def get_success_url(self):
        return reverse("currency-index")


class CurrencyDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(Currency, pk=kwargs.get("pk"))
        obj.delete()
        messages.success(request, f"{obj} deleted successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

# ------------------ Exchange Source ------------------

class ExchangeSourceListView(ListView):
    model = ExchangeSource
    context_object_name = "sources"
    template_name = "source/index.html"


class ExchangeSourceCreateView(SuccessMessageMixin, CreateView):
    model = ExchangeSource
    form_class = ExchangeSourceForm
    template_name = "source/create.html"
    success_message = "Source created successfully"

    def get_success_url(self):
        return reverse("source-index")


class ExchangeSourceUpdateView(SuccessMessageMixin, UpdateView):
    model = ExchangeSource
    form_class = ExchangeSourceForm
    template_name = "source/update.html"
    success_message = "Source updated successfully"

    def get_success_url(self):
        return reverse("source-index")


class ExchangeSourceDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(ExchangeSource, pk=kwargs.get("pk"))
        obj.delete()
        messages.success(request, f"{obj} deleted successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

# ------------------ Exchange Rate ------------------

class ExchangeRateListView(ListView):
    model = ExchangeRate
    context_object_name = "rates"
    template_name = "rate/index.html"


class ExchangeRateCreateView(SuccessMessageMixin, CreateView):
    model = ExchangeRate
    form_class = ExchangeRateForm
    template_name = "rate/create.html"
    success_message = "Rate created successfully"

    def get_success_url(self):
        return reverse("rate-index")


class ExchangeRateUpdateView(SuccessMessageMixin, UpdateView):
    model = ExchangeRate
    form_class = ExchangeRateForm
    template_name = "rate/update.html"
    success_message = "Rate updated successfully"

    def get_success_url(self):
        return reverse("rate-index")


class ExchangeRateDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(ExchangeRate, pk=kwargs.get("pk"))
        obj.delete()
        messages.success(request, f"{obj} deleted successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

# ------------------ User Exchange Rate ------------------

class UserExchangeRateListView(LoginRequiredMixin, ListView):
    model = UserExchangeRate
    context_object_name = "user_rates"
    template_name = "user_rate/index.html"

    def get_queryset(self):
        return UserExchangeRate.objects.filter(user=self.request.user)


class UserExchangeRateCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = UserExchangeRate
    form_class = UserExchangeRateForm
    template_name = "user_rate/create.html"
    success_message = "User exchange rate created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("user-rate-index")


class UserExchangeRateUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserExchangeRate
    form_class = UserExchangeRateForm
    template_name = "user_rate/update.html"
    success_message = "User exchange rate updated successfully"

    def get_queryset(self):
        return UserExchangeRate.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("user-rate-index")


class UserExchangeRateDeleteView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(UserExchangeRate, pk=kwargs.get("pk"), user=request.user)
        obj.delete()
        messages.success(request, f"{obj} deleted successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
    # ------------------ Transaction ------------------

class TransactionListView(ListView):
    model = Transaction
    context_object_name = "transactions"
    template_name = "transaction/index.html"
    ordering = ['-created_at']
    
class ExchangeProposalListView(ListView):
    model = ExchangeAgreement
    context_object_name = "proposals"
    template_name = "proposal/index.html"
    ordering = ['-id']
    
class ExchangeProposalCreateView(SuccessMessageMixin, CreateView):
    model = ExchangeProposal
    fields = ['amount']
    template_name = "proposal/create.html"
    success_message = "Exchange proposal created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("proposal-index")


class ExchangeProposalUpdateView(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        agreement = get_object_or_404(ExchangeAgreement, pk=kwargs.get("pk"))
        agreement.proposal.proposed_rate = request.POST.get("amount")
        agreement.proposal.save()
        messages.success(request, f"{agreement.proposal} updated successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class ExchangeProposalDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(ExchangeProposal, pk=kwargs.get("pk"), user=request.user)
        obj.delete()
        messages.success(request, f"{obj} deleted successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))