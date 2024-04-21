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
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from receivables.forms.transaction import TransactionForm
from receivables.models.transaction import Transaction


class TransactionListView(ListView):
    model = Transaction
    context_object_name = "transaction"
    template_name = "transaction/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TransactionCreateView(SuccessMessageMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transaction/create.html"
    success_message = "Transaction created successfully"

    def get_success_url(self):
        return reverse("transaction-index")


class TransactionDetailsView(DetailView):
    model = Transaction
    context_object_name = "transaction"
    template_name = "transaction/details.html"


class TransactionUpdateView(SuccessMessageMixin, UpdateView):
    model = Transaction
    context_object_name = "transaction"
    template_name = "transaction/update.html"
    form_class = TransactionForm
    success_message = "Transaction updated successfully"

    def get_success_url(self):
        return reverse("transaction-index")


class TransactionDeleteView(View):
    def get(self, request, **kwargs):
        transaction = get_object_or_404(Transaction, pk=kwargs.get('pk'))
        transaction.delete()
        messages.success(request,f'{transaction} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            


