
# Generic Views

from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import ApprovalGroupAction
from .forms import ApprovalGroupActionForm


class ApprovalGroupActionListView(SuccessMessageMixin, ListView):
    model = ApprovalGroupAction
    context_object_name = 'approval_group_actions'
    queryset = ApprovalGroupAction.objects.all()
    paginate_by = 25
    template_name = "approval_group_actions/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    
    
class ApprovalGroupActionCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalGroupAction
    context_object_name = 'approval_group_action'
    form_class = ApprovalGroupActionForm
    success_message = "Successfully created ApprovalGroupAction"
    template_name = 'approval_group_actions/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_group_actions-view')


class ApprovalGroupActionUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalGroupAction
    context_object_name = 'approval_group_action'
    form_class = ApprovalGroupActionForm 
    success_message = "Successfully updated ApprovalGroupAction"
    template_name = 'approval_group_actions/update.html'
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_group_action-view', args=(self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    

class ApprovalGroupActionDetailView(SuccessMessageMixin,DetailView):
    model = ApprovalGroupAction
    context_object_name = 'approval_group_action'
    template_name = 'approval_group_actions/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

class ApprovalGroupActionDeleteView(SuccessMessageMixin,DeleteView):
    model = ApprovalGroupAction
    form_class = ApprovalGroupActionForm
    template_name = "approval_group_actions/delete.html"
    success_message = 'Deleted ApprovalGroupAction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_group_actions-view')
    
