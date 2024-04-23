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
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from receivables.forms.province import ProvinceForm
from receivables.models.payment import Payment
from receivables.models.province import Province
from receivables.models.transaction import Transaction


class ProvinceListView(LoginRequiredMixin, ListView):
    model = Province
    context_object_name = "province"
    template_name = "province/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProvinceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Province
    form_class = ProvinceForm
    template_name = "province/create.html"
    success_message = "province created successfully"

    def get_success_url(self):
        return reverse("province-index")


class ProvinceDetailsView(LoginRequiredMixin, DetailView):
    model = Province
    context_object_name = "province"
    template_name = "province/details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.filter(user__province=self.object)
        payments = Payment.objects.filter(user__province=self.object)

        context['transactions'] = transactions
        context['payments'] = payments
        return context


class ProvinceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Province
    context_object_name = "province"
    template_name = "province/update.html"
    form_class = ProvinceForm
    success_message = "province updated successfully"

    def get_success_url(self):
        return reverse("province-index")


class ProvinceDeleteView(View):
    def get(self, request, **kwargs):
        dep = get_object_or_404(Province, pk=kwargs.get('pk'))
        dep.delete()
        messages.success(request,f'{dep} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))