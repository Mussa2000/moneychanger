
# Generic Views

from typing import Any
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import ApprovalGroup, ApprovalGroupProxy
from .forms import ApprovalGroupForm, ApprovalGroupProxyForm


class ApprovalGroupProxyDeleteView(SuccessMessageMixin,DeleteView):
    model = ApprovalGroupProxy
    
    template_name = "approval_groups/delete.html"
    success_message = 'Deleted Approval Group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket_proxy-view', args=(self.object.approval_ticket.pk,))
    

class ApprovalGroupProxyDetailView(SuccessMessageMixin,DetailView):
    model = ApprovalGroupProxy
    context_object_name = 'approval_group'
    template_name = 'approval_groups/detail_proxy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
class ApprovalGroupProxyCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalGroupProxy
    context_object_name = 'approval_group'
    form_class = ApprovalGroupProxyForm
    success_message = "Successfully created ApprovalGroup"
    template_name = 'approval_groups/create.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'].fields['approval_ticket'].initial = self.request.GET['approval_ticket_proxy']
        
        
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket_proxy-view', args=(self.object.approval_ticket.pk,))

class ApprovalGroupListView(SuccessMessageMixin, ListView):
    model = ApprovalGroup
    context_object_name = 'approval_groups'
    queryset = ApprovalGroup.objects.all()
    paginate_by = 25
    template_name = "approval_groups/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    
    
class ApprovalGroupCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalGroup
    context_object_name = 'approval_group'
    form_class = ApprovalGroupForm
    success_message = "Successfully created ApprovalGroup"
    template_name = 'approval_groups/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below
        context['form'].fields['approval_ticket'].initial = self.request.GET['approval_ticket']
        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket-view', args=(self.object.approval_ticket.pk,))


class ApprovalGroupUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalGroup
    context_object_name = 'approval_group'
    form_class = ApprovalGroupForm 
    success_message = "Successfully updated ApprovalGroup"
    template_name = 'approval_groups/update.html'
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_group-view', args=(self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    

class ApprovalGroupDetailView(SuccessMessageMixin,DetailView):
    model = ApprovalGroup
    context_object_name = 'approval_group'
    template_name = 'approval_groups/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

class ApprovalGroupDeleteView(SuccessMessageMixin,DeleteView):
    model = ApprovalGroup
    
    template_name = "approval_groups/delete.html"
    success_message = 'Deleted ApprovalGroup'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket-view', args=(self.object.approval_ticket.pk,))
    
