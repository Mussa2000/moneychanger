from django import forms
from .models import ApprovalGroupMark
from helpers import SubmitButtonHelper

class ApprovalGroupMarkForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = ApprovalGroupMark
        fields = "__all__"