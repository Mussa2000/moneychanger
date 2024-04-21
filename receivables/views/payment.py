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
from receivables.forms.payment import PaymentForm
from receivables.models.payment import Payment


class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    context_object_name = "payment"
    template_name = "payment/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PaymentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = "payment/create.html"
    success_message = "Payment created successfully"

    def get_success_url(self):
        return reverse("payment-index")


class PaymentDetailsView(LoginRequiredMixin, DetailView):
    model = Payment
    context_object_name = "payment"
    template_name = "payment/details.html"


class PaymentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Payment
    context_object_name = "payment"
    template_name = "payment/update.html"
    form_class = PaymentForm
    success_message = "Payment updated successfully"

    def get_success_url(self):
        return reverse("payment-index")


class PaymentDeleteView(View):
    def get(self, request, **kwargs):
        dep = get_object_or_404(Payment, pk=kwargs.get('pk'))
        dep.delete()
        messages.success(request,f'{dep} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))