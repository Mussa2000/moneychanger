from django import forms
from django.utils import timezone
from django.forms import ModelForm

from receivables.models.transaction import Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
        
        widgets = {
            "tra_date": forms.widgets.DateInput(attrs={"type": "date", "min": (timezone.now()).date()}),
        }


    def __init__(self,  *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"