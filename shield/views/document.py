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

from shield.forms.document import DocumentForm
from shield.models.document import Document


class DocumentListView(ListView):
    model = Document
    context_object_name = "document"
    template_name = "document/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DocumentCreateView(SuccessMessageMixin, CreateView):
    model = Document
    form_class = DocumentForm
    template_name = "document/create.html"
    success_message = "document created successfully"

    def get_success_url(self):
        return reverse("document-index")

class DocumentDetailsView(DetailView):
    model = Document
    context_object_name = "document"
    template_name = "document/details.html"


class DocumentUpdateView(SuccessMessageMixin, UpdateView):
    model = Document
    context_object_name = "document"
    template_name = "document/update.html"
    form_class = DocumentForm
    success_message = "document updated successfully"

    def get_success_url(self):
        return reverse("document-index")


class DocumentDeleteView(View):
    def get(self, request, **kwargs):
        obj = get_object_or_404(Document, pk=kwargs.get('pk'))
        obj.delete()
        messages.success(request,f'{obj} deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            


