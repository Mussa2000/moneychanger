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
from shield.models.alert import Alert
from shield.models.document import Document
from shield.models.folder import Folder

class AlertListView(ListView):
    model = Alert
    context_object_name = "alert"
    template_name = "alert/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AlertDetailsView(DetailView):
    model = Alert
    context_object_name = "alert"
    template_name = "alert/details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



