from django import forms
from .models import ApprovalTicket, ApprovalTicketProxy
from approval_engine.shared.helpers import SubmitButtonHelper
from django.apps import apps
from django.db.models import QuerySet


class ApprovalTicketForm(SubmitButtonHelper, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApprovalTicketForm, self).__init__(*args, **kwargs)
        # self.fields["approval_actions"].widget.attrs[
        #     "class"
        # ] = "form-control js-select2 multiple"
        # self.fields["approval_actions"].widget.attrs["data-search"] = "on"

    class Meta:
        model = ApprovalTicket
        fields = "__all__"
        # exclude = ("is_approved",)
        widgets = {
            "model_module_location": forms.HiddenInput(),
            "model_record_id": forms.HiddenInput(),
            "created_by": forms.HiddenInput(),
        }
        
class ApprovalTicketProxyForm(SubmitButtonHelper, forms.ModelForm):
    
    class Meta:
        model = ApprovalTicketProxy
        fields = '__all__'

class SelectModelForm(SubmitButtonHelper, forms.Form):
    model_choices = [
        (model._meta.label, model._meta.verbose_name_plural.title())
        for model in apps.get_models()
        if hasattr(model, "is_assignable")
    ]
    model = forms.ChoiceField(
        choices=model_choices,
        widget=forms.Select(
            attrs={"class": "form-select js-select2", "data-search": "on"}
        ),
    )


class SelectModelRecordForm(SubmitButtonHelper, forms.Form):
    model_record_id = forms.ModelChoiceField(
        queryset=QuerySet(),
        widget=forms.Select(
            attrs={"class": "form-select js-select2", "data-search": "on"}
        ),
    )
