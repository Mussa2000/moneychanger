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

from receivables.forms.product import ProductForm
from receivables.models.product import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = "product"
    template_name = "product/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/create.html"
    success_message = "Product created successfully"

    def get_success_url(self):
        return reverse("product-index")


class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product/details.html"


class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    context_object_name = "product"
    template_name = "product/update.html"
    form_class = ProductForm
    success_message = "Product updated successfully"

    def get_success_url(self):
        return reverse("product-index")


class ProductDeleteView(View):
    def get(self, request, **kwargs):
        dep = get_object_or_404(Product, pk=kwargs.get('pk'))
        dep.delete()
        messages.success(request,f'{dep} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))