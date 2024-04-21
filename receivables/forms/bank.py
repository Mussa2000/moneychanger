from django import forms
from django.utils import timezone
from django.forms import ModelForm
from receivables.models.bank import Bank

class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs):
        super(BankForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"