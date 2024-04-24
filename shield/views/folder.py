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

from shield.forms.folder import FolderForm
from shield.models.folder import Folder


class FolderListView(ListView):
    model = Folder
    context_object_name = "folder"
    template_name = "folder/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FolderCreateView(SuccessMessageMixin, CreateView):
    model = Folder
    form_class = FolderForm
    template_name = "folder/create.html"
    success_message = "folder created successfully"

    def get_success_url(self):
        return reverse("folder-index")

class FolderDetailsView(DetailView):
    model = Folder
    context_object_name = "folder"
    template_name = "folder/details.html"


class FolderUpdateView(SuccessMessageMixin, UpdateView):
    model = Folder
    context_object_name = "folder"
    template_name = "folder/update.html"
    form_class = FolderForm
    success_message = "folder updated successfully"

    def get_success_url(self):
        return reverse("folder-index")


class FolderDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(Folder, pk=kwargs.get('pk'))
        obj.delete()
        messages.success(request,f'{obj} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            


