from django import forms
from .models import ApprovalGroupAction
from helpers import SubmitButtonHelper

class ApprovalGroupActionForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = ApprovalGroupAction
        fields = "__all__"