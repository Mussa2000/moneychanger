
# Generic Views

from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import ApprovalAction
from .forms import ApprovalActionForm


class ApprovalActionListView(SuccessMessageMixin, ListView):
    model = ApprovalAction
    context_object_name = 'approval_actions'
    queryset = ApprovalAction.objects.all()
    paginate_by = 25
    template_name = "approval_actions/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    
    
class ApprovalActionCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalAction
    context_object_name = 'approval_action'
    form_class = ApprovalActionForm
    success_message = "Successfully created ApprovalAction"
    template_name = 'approval_actions/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_actions-view')


class ApprovalActionUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalAction
    context_object_name = 'approval_action'
    form_class = ApprovalActionForm 
    success_message = "Successfully updated ApprovalAction"
    template_name = 'approval_actions/update.html'
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_action-view', args=(self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    

class ApprovalActionDetailView(SuccessMessageMixin,DetailView):
    model = ApprovalAction
    context_object_name = 'approval_action'
    template_name = 'approval_actions/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

class ApprovalActionDeleteView(SuccessMessageMixin,DeleteView):
    model = ApprovalAction
    form_class = ApprovalActionForm
    template_name = "approval_actions/delete.html"
    success_message = 'Deleted ApprovalAction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_actions-view')
    
