
# Generic Views

from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import ApprovalMark
from .forms import ApprovalMarkForm


class ApprovalMarkListView(SuccessMessageMixin, ListView):
    model = ApprovalMark
    context_object_name = 'approval_marks'
    queryset = ApprovalMark.objects.all()
    paginate_by = 25
    template_name = "approval_marks/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    
    
class ApprovalMarkCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalMark
    context_object_name = 'approval_mark'
    form_class = ApprovalMarkForm
    success_message = "Successfully created ApprovalMark"
    template_name = 'approval_marks/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below
        context['form'].fields['approval_level'].initial = self.request.GET['approval_level']
        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket-view', args=(self.object.approval_level.approval_group.approval_ticket.pk,))


class ApprovalMarkUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalMark
    context_object_name = 'approval_mark'
    form_class = ApprovalMarkForm 
    success_message = "Successfully updated ApprovalMark"
    template_name = 'approval_marks/update.html'
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_mark-view', args=(self.object.id,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    

class ApprovalMarkDetailView(SuccessMessageMixin,DetailView):
    model = ApprovalMark
    context_object_name = 'approval_mark'
    template_name = 'approval_marks/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

class ApprovalMarkDeleteView(SuccessMessageMixin,DeleteView):
    model = ApprovalMark
    form_class = ApprovalMarkForm
    template_name = "approval_marks/delete.html"
    success_message = 'Deleted ApprovalMark'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_marks-view')
    
