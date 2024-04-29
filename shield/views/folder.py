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
from shield.helpers.action_logger import log_action
from shield.models.document import Document
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
        log_action(self.request.user, "Folder Creation", str(self.object.name))
        return reverse("folder-index")

class FolderDetailsView(DetailView):
    model = Folder
    context_object_name = "folder"
    template_name = "folder/details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        log_action(self.request.user, "Viewed folder details", str(self.object.name))
        documents = Document.objects.filter(folder = self.object)
        
        context['documents'] = documents
        return context


class FolderUpdateView(SuccessMessageMixin, UpdateView):
    model = Folder
    context_object_name = "folder"
    template_name = "folder/update.html"
    form_class = FolderForm
    success_message = "folder updated successfully"

    def get_success_url(self):
        log_action(self.request.user, "Folder Update", str(self.object.name))
        return reverse("folder-index")


class FolderDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(Folder, pk=kwargs.get('pk'))
        obj.delete()
        log_action(request.user, "Document Deletion", str(self.object.name))
        messages.success(request,f'{obj} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            


