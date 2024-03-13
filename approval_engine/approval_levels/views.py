# Generic Views

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from django.contrib.messages.views import SuccessMessageMixin

from approval_engine.approval_groups.models import ApprovalGroup, ApprovalGroupProxy

from .models import ApprovalLevel, ApprovalLevelProxy
from .forms import ApprovalLevelForm, ApprovalLevelProxyForm
from django.contrib import messages

class ApprovalLevelProxyDeleteView(SuccessMessageMixin, DeleteView):
    model = ApprovalLevelProxy
    
    template_name = "approval_levels/delete.html"
    success_message = "Deleted ApprovalLevel"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    def get_success_url(self) -> str:
        return reverse(
            "detail-approval_group_proxy-view", args=(self.object.approval_group.pk,)
        )
        
class ApprovalLevelProxyUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalLevelProxy
    context_object_name = "approval_level"
    form_class = ApprovalLevelProxyForm
    success_message = "Successfully updated ApprovalLevel"
    template_name = "approval_levels/update.html"

    def get_success_url(self) -> str:
        return reverse(
            "detail-approval_group_proxy-view", args=(self.object.approval_group.pk,)
        )
        
class ApprovalLevelProxyCreateView(SuccessMessageMixin, CreateView):
    model = ApprovalLevelProxy
    context_object_name = "approval_level"
    form_class = ApprovalLevelProxyForm
    success_message = "Successfully created Approval Level"
    template_name = "approval_levels/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below
        approval_group_pk = self.request.GET["approval_group"]
        approval_group = ApprovalGroupProxy.objects.get(pk=approval_group_pk)
        context["form"].fields["approval_group"].initial = approval_group_pk
        context["form"].fields["index"].initial = (
            approval_group.approval_levels.count() + 1
        )
        context["form"].fields[
            "name"
        ].initial = f"Approval Level {approval_group.approval_levels.count() + 1}"
        # return context
        return context
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_group_proxy-view', args=(self.object.approval_group.pk,))
    
    
class ApprovalLevelListView(SuccessMessageMixin, ListView):
    model = ApprovalLevel
    context_object_name = "approval_levels"
    queryset = ApprovalLevel.objects.all()
    paginate_by = 25
    template_name = "approval_levels/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context


class ApprovalLevelCreateView(SuccessMessageMixin, CreateView):
    model = ApprovalLevel
    context_object_name = "approval_level"
    form_class = ApprovalLevelForm
    success_message = "Successfully created ApprovalLevel"
    template_name = "approval_levels/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below
        approval_group_pk = self.request.GET["approval_group"]
        approval_group = ApprovalGroup.objects.get(pk=approval_group_pk)
        context["form"].fields["approval_group"].initial = approval_group_pk
        context["form"].fields["index"].initial = (
            approval_group.approval_levels.count() + 1
        )
        context["form"].fields[
            "name"
        ].initial = f"Approval Level {approval_group.approval_levels.count() + 1}"
        # return context
        return context

    def get_success_url(self) -> str:
        return reverse(
            "detail-approval_group-view", args=(self.object.approval_group.pk,)
        )


class ApprovalLevelUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalLevel
    context_object_name = "approval_level"
    form_class = ApprovalLevelForm
    success_message = "Successfully updated ApprovalLevel"
    template_name = "approval_levels/update.html"

    def get_success_url(self) -> str:
        return reverse(
            "detail-approval_group-view", args=(self.object.approval_group.pk,)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context


class ApprovalLevelDetailView(SuccessMessageMixin, DetailView):
    model = ApprovalLevel
    context_object_name = "approval_level"
    template_name = "approval_levels/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context


class ApprovalLevelDeleteView(SuccessMessageMixin, DeleteView):
    model = ApprovalLevel
    
    template_name = "approval_levels/delete.html"
    success_message = "Deleted ApprovalLevel"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inject extra data into context object below

        # return context
        return context

    def get_success_url(self) -> str:
        return reverse(
            "detail-approval_group-view", args=(self.object.approval_group.pk,)
        )


def shift_approval_level_to_up(request, approval_level_pk, *args, **kwargs):
    approval_level = ApprovalLevel.objects.get(pk=approval_level_pk)
    if approval_level:
        # Get the next record based on the current index
        next_record = (
            ApprovalLevel.objects.filter(
                index__lt=approval_level.index,
                approval_group=approval_level.approval_group,
            )
            .order_by("index")
            .last()
        )

        if next_record:
            # Swap index and name values
            approval_level.index, next_record.index = (
                next_record.index,
                approval_level.index,
            )
            approval_level.name, next_record.name = (
                next_record.name,
                approval_level.name,
            )

            approval_level.save()
            next_record.save()
            messages.success(request, 'Moved Level Up')

    return redirect(
        reverse("detail-approval_group-view", args=(approval_level.approval_group.pk,))
    )

def shift_approval_level_to_down(request, approval_level_pk, *args, **kwargs):
    # Use get() directly to retrieve the current record
    approval_level = ApprovalLevel.objects.get(pk=approval_level_pk)

    # Get the previous record based on the current index
    prev_record = (
        ApprovalLevel.objects.filter(
            index__gt=approval_level.index, approval_group=approval_level.approval_group
        )
        .order_by("-index")
        .last()
    )
    

    if prev_record:
        # Swap index and name values
        approval_level.index, prev_record.index = (
            prev_record.index,
            approval_level.index,
        )
        approval_level.name, prev_record.name = prev_record.name, approval_level.name

        # Save both the current record and the previous record
        approval_level.save()
        prev_record.save()
        messages.success(request, 'Moved Level Down')
    # Redirect to the appropriate view
    return redirect(
        reverse("detail-approval_group-view", args=(approval_level.approval_group.pk,))
    )



#PROXIES

def shift_approval_level_proxy_to_up(request, approval_level_proxy_pk, *args, **kwargs):
    approval_level_proxy = ApprovalLevelProxy.objects.get(pk=approval_level_proxy_pk)
    if approval_level_proxy:
        # Get the next record based on the current index
        next_record = (
            ApprovalLevelProxy.objects.filter(
                index__lt=approval_level_proxy.index,
                approval_group=approval_level_proxy.approval_group,
            )
            .order_by("index")
            .last()
        )

        if next_record:
            # Swap index and name values
            approval_level_proxy.index, next_record.index = (
                next_record.index,
                approval_level_proxy.index,
            )
            approval_level_proxy.name, next_record.name = (
                next_record.name,
                approval_level_proxy.name,
            )

            approval_level_proxy.save()
            next_record.save()
            messages.success(request, 'Moved Level Up')

    return redirect(
        reverse("detail-approval_group_proxy-view", args=(approval_level_proxy.approval_group.pk,))
    )

def shift_approval_level_proxy_to_down(request, approval_level_proxy_pk, *args, **kwargs):
    # Use get() directly to retrieve the current record
    approval_level_proxy = ApprovalLevelProxy.objects.get(pk=approval_level_proxy_pk)

    # Get the previous record based on the current index
    prev_record = (
        ApprovalLevelProxy.objects.filter(
            index__gt=approval_level_proxy.index, approval_group=approval_level_proxy.approval_group
        )
        .order_by("-index")
        .last()
    )
    

    if prev_record:
        # Swap index and name values
        approval_level_proxy.index, prev_record.index = (
            prev_record.index,
            approval_level_proxy.index,
        )
        approval_level_proxy.name, prev_record.name = prev_record.name, approval_level_proxy.name

        # Save both the current record and the previous record
        approval_level_proxy.save()
        prev_record.save()
        messages.success(request, 'Moved Level Down')
    # Redirect to the appropriate view
    return redirect(
        reverse("detail-approval_group_proxy-view", args=(approval_level_proxy.approval_group.pk,))
    )
