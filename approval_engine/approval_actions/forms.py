from django import forms
from .models import ApprovalAction
from helpers import SubmitButtonHelper

class ApprovalActionForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = ApprovalAction
        fields = "__all__"