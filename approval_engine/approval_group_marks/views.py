
# Generic Views

from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import ApprovalGroupMark
from .forms import ApprovalGroupMarkForm


class ApprovalGroupMarkListView(SuccessMessageMixin, ListView):
    model = ApprovalGroupMark
    context_object_name = 'approval_group_marks'
    queryset = ApprovalGroupMark.objects.all()
    paginate_by = 25
    template_name = "approval_group_marks/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    
    
class ApprovalGroupMarkCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalGroupMark
    context_object_name = 'approval_group_mark'
    form_class = ApprovalGroupMarkForm
    success_message = "Successfully created ApprovalGroupMark"
    template_name = 'approval_group_marks/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_group_marks-view')


class ApprovalGroupMarkUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalGroupMark
    context_object_name = 'approval_group_mark'
    form_class = ApprovalGroupMarkForm 
    success_message = "Successfully updated ApprovalGroupMark"
    template_name = 'approval_group_marks/update.html'
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_group_mark-view', args=(self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    

class ApprovalGroupMarkDetailView(SuccessMessageMixin,DetailView):
    model = ApprovalGroupMark
    context_object_name = 'approval_group_mark'
    template_name = 'approval_group_marks/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

class ApprovalGroupMarkDeleteView(SuccessMessageMixin,DeleteView):
    model = ApprovalGroupMark
    form_class = ApprovalGroupMarkForm
    template_name = "approval_group_marks/delete.html"
    success_message = 'Deleted ApprovalGroupMark'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_group_marks-view')
    
