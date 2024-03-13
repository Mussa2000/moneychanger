# Generic Views

from typing import Any
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
    TemplateView,
)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.apps import apps
from django.shortcuts import redirect
from approval_engine.approval_group_levels.models import ApprovalGroupLevel
from approval_engine.approval_group_marks.models import ApprovalGroupMark
from approval_engine.approval_levels.models import ApprovalLevel
from approval_engine.shared.helpers.load_module import load_model_from_module
from .models import ApprovalTicket, ApprovalTicketProxy
from approval_engine.approvers.models import Approver
from django.conf import settings
from approval_engine.approval_marks.models import ApprovalMark
from .forms import ApprovalTicketProxyForm, ApprovalTicketForm, SelectModelForm, SelectModelRecordForm
from accounts.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class ApprovalTicketProxyListView(SuccessMessageMixin, ListView):
    model = ApprovalTicket
    context_object_name = "approval_tickets"
    queryset = ApprovalTicketProxy.objects.all()
    paginate_by = 25
    template_name = "approval_tickets/list_proxy.html"
    
class ApprovalTicketProxyCreateView(SuccessMessageMixin, CreateView):
    model = ApprovalTicketProxy
    context_object_name = "approval_ticket"
    form_class = ApprovalTicketProxyForm
    success_message = "Successfully created ApprovalTicket"
    template_name = "approval_tickets/create.html"
    
    def get_success_url(self) -> str:
        return reverse('detail-approval_ticket_proxy-view', args=(self.object.pk,))

class ApprovalTicketProxyDetailView(SuccessMessageMixin, DetailView):
    model = ApprovalTicketProxy
    context_object_name = "approval_ticket_proxy"
    form_class = ApprovalTicketProxyForm
    template_name = "approval_tickets/detail_proxy.html"

class ApprovalTicketListView(SuccessMessageMixin, ListView):
    model = ApprovalTicket
    context_object_name = "approval_tickets"
    queryset = ApprovalTicket.objects.all()
    paginate_by = 25
    template_name = "approval_tickets/list.html"

    # views.py


class UserApprovalTicketDetailView(TemplateView):
    template_name = "approval_tickets/approval_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = CustomUser.objects.filter(pk=self.kwargs["pk"]).first()
        if user: 
            context['tickets'] = [ticket for ticket in ApprovalTicket.objects.filter(is_approved=False).all() if user.approver in ticket.approver_roles()]
        return context


class ApprovalTicketCreateView(SuccessMessageMixin, CreateView):
    model = ApprovalTicket
    context_object_name = "approval_ticket"
    form_class = ApprovalTicketForm
    success_message = "Successfully created ApprovalTicket"
    template_name = "approval_tickets/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        module_location = self.request.GET["model_label"].split(".")[0] + ".loader"
        module_record_id = self.request.GET["model_record_id"]
        context["form"].fields["model_module_location"].initial = module_location
        context["form"].fields["model_record_id"].initial = module_record_id
        context["form"].fields["created_by"].initial = self.request.user

        context["preloaded_model"] = load_model_from_module(
            module_location, module_record_id
        )

        return context

    def get_success_url(self) -> str:
        return reverse("list-approval_tickets-view")


class ApprovalTicketUpdateView(SuccessMessageMixin, UpdateView):
    model = ApprovalTicket
    context_object_name = "approval_ticket"
    form_class = ApprovalTicketForm
    success_message = "Successfully updated ApprovalTicket"
    template_name = "approval_tickets/update.html"

    def get_success_url(self) -> str:
        return reverse("detail-approval_ticket-view", args=(self.object.id,))


class ApprovalTicketDetailView(SuccessMessageMixin, LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('account_login')
    model = ApprovalTicket
    context_object_name = "approval_ticket"
    template_name = "approval_tickets/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        has_approval_mark_permission = True
        
        group_level_awaiting_approval = self.object.approval_group_levels.filter(
            approval_group_marks__isnull=True,
        ).order_by('index').first()
        
        context['group_level_awaiting_approval'] = group_level_awaiting_approval
        
        try:
            current_user_level_in_group_matches = group_level_awaiting_approval.approval_group.approval_levels.filter(approver__user=self.request.user)
            
            if current_user_level_in_group_matches.count() == 0:
                has_approval_mark_permission = False
            else:
                current_group_level = current_user_level_in_group_matches.first()
                current_group = current_group_level.approval_group
                # get the current approving level 
                level_awaiting_approval = current_group.approval_levels.filter(approval_mark__isnull=True).order_by('index').first()
                if level_awaiting_approval.approver.user != self.request.user:
                    has_approval_mark_permission = False
                # my lovely additionals 
                next_approval_group_level = self.object.approval_group_levels.filter(
                    approval_group_marks__isnull=True,
                    index__gt=current_group_level.index
                ).order_by('index').first()
                
                if next_approval_group_level:
                    context['next_approval_group_level'] = next_approval_group_level
                    context['next_approval_group'] = next_approval_group_level.approval_group
                context['current_group_level'] = current_group_level
                context['current_group'] = current_group
                
                
            
            context["has_approval_mark_permission"] = has_approval_mark_permission
            return context
        except Exception as e:
            context["has_approval_mark_permission"] = False
            return context


# views.py


class ApprovalTicketMarksDetailView(SuccessMessageMixin, DetailView):
    model = ApprovalTicket
    context_object_name = "ticket"
    template_name = "approval_marks/detail.html"


class ApprovalTicketDeleteView(SuccessMessageMixin, DeleteView):
    model = ApprovalTicket
    template_name = "approval_tickets/delete.html"
    success_message = "Deleted ApprovalTicket"

    def get_success_url(self) -> str:
        return reverse("list-approval_ticket-view")


def select_model_form_view(request):
    if request.method == "POST":
        form = SelectModelForm(request.POST)
        if form.is_valid():
            return redirect(
                reverse(
                    "select-model_record-view",
                    kwargs={
                        "model_label": form.cleaned_data["model"],
                    },
                )
            )
    else:
        form = SelectModelForm()

    return render(request, "approval_tickets/select_model_form.html", {"form": form})


def select_model_record_form_view(request, model_label):
    if request.method == "POST":
        form = SelectModelRecordForm(request.POST)

        model_record_id = form.data["model_record_id"]
        return redirect(
            reverse("create-approval_ticket-view")
            + f"?model_record_id={model_record_id}&"
            + f"model_label={model_label}"
        )
    else:
        model_choices = [(model._meta.label, model) for model in apps.get_models()]
        selected_model = [model for model in model_choices if model[0] == model_label][
            0
        ][1]

        form = SelectModelRecordForm()
        form.fields["model_record_id"].queryset = selected_model.objects.all()
        selected_model.objects.all()

    return render(
        request, "approval_tickets/select_model_record_form.html", {"form": form}
    )


from django.http import HttpResponse, Http404
from django.views.generic import View
from django.conf import settings
import os


class AttachmentDownloadView(View):
    def get(self, request, approval_mark, *args, **kwargs):
        attachment = ApprovalMark.objects.get(pk=approval_mark)

        return self.download_attachment(attachment.na)

    def download_attachment(self, filename):
        attachment_filepath = os.path.join(
            settings.MEDIA_ROOT, "approval_marks", filename
        )

        if not os.path.exists(attachment_filepath):
            raise Http404("Attachment does not exist")

        with open(attachment_filepath, "rb") as rf:
            response = HttpResponse(rf.read(), content_type="application/octet-stream")
            response[
                "Content-Disposition"
            ] = f'attachment; filename="{os.path.basename(attachment_filepath)}"'
            return response
