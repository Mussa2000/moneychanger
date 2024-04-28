import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
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
from shield.models.alert import Alert
from shield.models.document import Document
from shield.models.folder import Folder
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

class DocumentListView(ListView):
    model = Document
    context_object_name = "document"
    template_name = "document/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DocumentCreateView(SuccessMessageMixin, View):
    def get(self, request, pk):
        folder = get_object_or_404(Folder, pk=pk)
        form = DocumentForm()
        return render(request, "document/create.html", {"folder": folder, "form": form })
    
    def post(self, request, pk):
        folder = get_object_or_404(Folder, pk=pk)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():          
            document = form.save(commit=False)
            document.save()

            if document:
                messages.success(request,'Document Successfully')
                return redirect('folder-details', pk = folder.pk )
            else:
                messages.warning(request,'Error placing bid')
                return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.warning(request, form.errors)
            return render(request, "document/create.html", {"folder": folder, "form": form})



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
        if request.user not in obj.folder.users.all():
            messages.warning(request,f'You are not authorized to delete this document')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        else:
            obj.delete()
            messages.success(request,f'{obj} deleted successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class DocumentDownloadView(View):
    def get(self, request, pk):
        # Retrieve the document object
        document = get_object_or_404(Document, pk=pk)

        # Check if the user has permission to download the document
        if request.user not in document.folder.users.all():
            messages.warning(request, 'You are not authorized to download this document')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        try:
            # Log the download action
            download_time = timezone.now() + timedelta(hours=2)
            action_message = f"Document '{document.name}' was downloaded by user '{request.user.username}' at {download_time}."
            Alert.objects.create(user=request.user, name="Document Download", message=action_message)

            # Return the file response
            file_path = document.path.path
            response = FileResponse(open(file_path, 'rb'), as_attachment=True)
            return response
        except FileNotFoundError:
            raise Http404