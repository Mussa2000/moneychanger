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

from receivables.forms.bank import BankForm
from receivables.models.bank import Bank


class BankListView(ListView):
    model = Bank
    context_object_name = "Bank"
    template_name = "Bank/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BankCreateView(SuccessMessageMixin, CreateView):
    model = Bank
    form_class = BankForm
    template_name = "bank/create.html"
    success_message = "Bank created successfully"

    def get_success_url(self):
        return reverse("bank-index")


class BankDetailsView(DetailView):
    model = Bank
    context_object_name = "bank"
    template_name = "bank/details.html"


class BankUpdateView(SuccessMessageMixin, UpdateView):
    model = Bank
    context_object_name = "bank"
    template_name = "bank/update.html"
    form_class = BankForm
    success_message = "Bank updated successfully"

    def get_success_url(self):
        return reverse("bank-index")


class BankDeleteView(View):
    def get(self, request, **kwargs):
        bank = get_object_or_404(Bank, pk=kwargs.get('pk'))
        bank.delete()
        messages.success(request,f'{bank} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            


