from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, View
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Currency, ExchangeSource, ExchangeRate
from .forms import CurrencyForm, ExchangeSourceForm, ExchangeRateForm

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
