from django import forms
from .models import Approver
from helpers import SubmitButtonHelper

class ApproverForm( SubmitButtonHelper, forms.ModelForm ):
    class Meta:
        model = Approver
        fields = "__all__"