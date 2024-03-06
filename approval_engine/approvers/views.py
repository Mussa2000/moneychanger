
# Generic Views

from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Approver
from .forms import ApproverForm


class ApproverListView(SuccessMessageMixin, ListView):
    model = Approver
    context_object_name = 'approvers'
    queryset = Approver.objects.all()
    paginate_by = 25
    template_name = "approvers/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    
    
class ApproverCreateView(SuccessMessageMixin,CreateView):
    model = Approver
    context_object_name = 'approver'
    form_class = ApproverForm
    success_message = "Successfully created Approver"
    template_name = 'approvers/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approvers-view')


class ApproverUpdateView(SuccessMessageMixin, UpdateView):
    model = Approver
    context_object_name = 'approver'
    form_class = ApproverForm 
    success_message = "Successfully updated Approver"
    template_name = 'approvers/update.html'
    
    def get_success_url(self) -> str:
        return reverse('detail-approver-view', args=(self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    

class ApproverDetailView(SuccessMessageMixin,DetailView):
    model = Approver
    context_object_name = 'approver'
    template_name = 'approvers/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

class ApproverDeleteView(SuccessMessageMixin,DeleteView):
    model = Approver
    form_class = ApproverForm
    template_name = "approvers/delete.html"
    success_message = 'Deleted Approver'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approvers-view')
    
