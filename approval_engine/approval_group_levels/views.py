
# Generic Views

from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from approval_engine.approval_tickets.models import ApprovalTicket, ApprovalTicketProxy

from .models import ApprovalGroupLevel, ApprovalGroupLevelProxy
from .forms import ApprovalGroupLevelForm, ApprovalGroupLevelProxyForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import ApprovalGroupLevel


class ApprovalGroupLevelProxyCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalGroupLevelProxy
    context_object_name = 'approval_group_level'
    form_class = ApprovalGroupLevelProxyForm
    success_message = "Successfully created ApprovalGroupLevel"
    template_name = 'approval_group_levels/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below
        approval_group_pk = int(self.request.GET['approval_group_proxy'])
        approval_ticket_proxy_pk = self.request.GET['approval_ticket_proxy']
        
        approval_ticket = ApprovalTicketProxy.objects.get(pk=approval_ticket_proxy_pk)
        approval_group_level_index = approval_ticket.approval_group_levels.count() + 1
        context['form'].fields['approval_ticket'].initial = approval_ticket.pk
        context['form'].fields['approval_group'].initial = self.request.GET['approval_group_proxy']
        context['form'].fields['index'].initial = approval_group_level_index
        context['form'].fields['name'].initial = f'Approval Group Level {approval_group_level_index}'
        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket_proxy-view', args=(self.object.approval_ticket.pk,))
    
    
    
class ApprovalGroupLevelListView(SuccessMessageMixin, ListView):
    model = ApprovalGroupLevel
    context_object_name = 'approval_group_levels'
    queryset = ApprovalGroupLevel.objects.all()
    paginate_by = 25
    template_name = "approval_group_levels/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    
    
class ApprovalGroupLevelCreateView(SuccessMessageMixin,CreateView):
    model = ApprovalGroupLevel
    context_object_name = 'approval_group_level'
    form_class = ApprovalGroupLevelForm
    success_message = "Successfully created ApprovalGroupLevel"
    template_name = 'approval_group_levels/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below
        approval_group_pk = int(self.request.GET['approval_group'])
        approval_ticket_pk = self.request.GET['approval_ticket']
        
        approval_ticket = ApprovalTicket.objects.get(pk=approval_ticket_pk)
        approval_group_level_index = approval_ticket.approval_group_levels.count() + 1
        context['form'].fields['approval_ticket'].initial = approval_ticket.pk
        context['form'].fields['approval_group'].initial = self.request.GET['approval_group']
        context['form'].fields['index'].initial = approval_group_level_index
        context['form'].fields['name'].initial = f'Approval Group Level {approval_group_level_index}'
        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket-view', args=(self.object.approval_ticket.pk,))


class ApprovalGroupLevelUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalGroupLevel
    context_object_name = 'approval_group_level'
    form_class = ApprovalGroupLevelForm 
    success_message = "Successfully updated ApprovalGroupLevel"
    template_name = 'approval_group_levels/update.html'
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket-view', args=(self.object.approval_ticket.pk,))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    

class ApprovalGroupLevelDetailView(SuccessMessageMixin,DetailView):
    model = ApprovalGroupLevel
    context_object_name = 'approval_group_level'
    template_name = 'approval_group_levels/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

class ApprovalGroupLevelDeleteView(SuccessMessageMixin,DeleteView):
    model = ApprovalGroupLevel
    form_class = ApprovalGroupLevelForm
    template_name = "approval_group_levels/delete.html"
    success_message = 'Deleted ApprovalGroupLevel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('list-approval_group_levels-view')
    

from django.db.models import Q

def shift_approval_group_level_to_right(request, approval_group_level_pk, *args, **kwargs):
    approval_group_level = ApprovalGroupLevel.objects.get(pk=approval_group_level_pk)
    if approval_group_level:
        # Get the next record based on the current index and the same approval group
        next_record = ApprovalGroupLevel.objects.filter(
            Q(index__gt=approval_group_level.index) 
            &
            Q(approval_ticket=approval_group_level.approval_ticket)
        ).order_by('index').first()
        
        if next_record:
            # Swap index and name values
            approval_group_level.index, next_record.index = next_record.index, approval_group_level.index
            approval_group_level.name, next_record.name = next_record.name, approval_group_level.name

            approval_group_level.save()
            next_record.save()

    return redirect(reverse('detail-approval_ticket-view', args=(approval_group_level.approval_ticket.pk,)))


def shift_approval_group_level_to_left(request, approval_group_level_pk, *args, **kwargs):
    # Get the current record
    approval_group_level = get_object_or_404(ApprovalGroupLevel, pk=approval_group_level_pk)

    # Get the previous record based on the current index and the same approval group
    prev_record = ApprovalGroupLevel.objects.filter(
        Q(index__lt=approval_group_level.index) &
        Q(approval_ticket=approval_group_level.approval_ticket)
    ).order_by('-index').first()

    if prev_record:
        # Swap index and name values
        approval_group_level.index, prev_record.index = prev_record.index, approval_group_level.index
        approval_group_level.name, prev_record.name = prev_record.name, approval_group_level.name

        # Save both the current record and the previous record
        approval_group_level.save()
        prev_record.save()

    # Redirect to the appropriate view
    return redirect(reverse('detail-approval_ticket-view', args=(approval_group_level.approval_ticket.pk,)))




# Proxies

def shift_approval_group_level_proxy_to_right(request, approval_group_level_proxy_pk, *args, **kwargs):
    approval_group_level_proxy = ApprovalGroupLevelProxy.objects.get(pk=approval_group_level_proxy_pk)
    if approval_group_level_proxy:
        # Get the next record based on the current index and the same approval group
        next_record = ApprovalGroupLevelProxy.objects.filter(
            Q(index__gt=approval_group_level_proxy.index) 
            &
            Q(approval_ticket=approval_group_level_proxy.approval_ticket)
        ).order_by('index').first()
        
        if next_record:
            # Swap index and name values
            approval_group_level_proxy.index, next_record.index = next_record.index, approval_group_level_proxy.index
            approval_group_level_proxy.name, next_record.name = next_record.name, approval_group_level_proxy.name

            approval_group_level_proxy.save()
            next_record.save()

    return redirect(reverse('detail-approval_ticket_proxy-view', args=(approval_group_level_proxy.approval_ticket.pk,)))


def shift_approval_group_level_proxy_to_left(request, approval_group_level_proxy_pk, *args, **kwargs):
    # Get the current record
    approval_group_level_proxy = get_object_or_404(ApprovalGroupLevelProxy, pk=approval_group_level_proxy_pk)

    # Get the previous record based on the current index and the same approval group
    prev_record = ApprovalGroupLevelProxy.objects.filter(
        Q(index__lt=approval_group_level_proxy.index) &
        Q(approval_ticket=approval_group_level_proxy.approval_ticket)
    ).order_by('-index').first()

    if prev_record:
        # Swap index and name values
        approval_group_level_proxy.index, prev_record.index = prev_record.index, approval_group_level_proxy.index
        approval_group_level_proxy.name, prev_record.name = prev_record.name, approval_group_level_proxy.name

        # Save both the current record and the previous record
        approval_group_level_proxy.save()
        prev_record.save()

    # Redirect to the appropriate view
    return redirect(reverse('detail-approval_ticket_proxy-view', args=(approval_group_level_proxy.approval_ticket.pk,)))
