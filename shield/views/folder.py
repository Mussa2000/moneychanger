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
from assets.forms.asset import AssetForm
from assets.models.asset import Asset


class AssetListView(ListView):
    model = Asset
    context_object_name = "asset"
    template_name = "asset/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AssetCreateView(SuccessMessageMixin, CreateView):
    model = Asset
    form_class = AssetForm
    template_name = "asset/create.html"
    success_message = "asset created successfully"

    def get_success_url(self):
        return reverse("asset-index")

class AssetDetailsView(DetailView):
    model = Asset
    context_object_name = "asset"
    template_name = "asset/details.html"


class AssetUpdateView(SuccessMessageMixin, UpdateView):
    model = Asset
    context_object_name = "asset"
    template_name = "asset/update.html"
    form_class = AssetForm
    success_message = "asset updated successfully"

    def get_success_url(self):
        return reverse("asset-index")


class AssetDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(Asset, pk=kwargs.get('pk'))
        obj.delete()
        messages.success(request,f'{obj} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            


