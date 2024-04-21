from django import forms
from django.utils import timezone
from django.forms import ModelForm

from receivables.models.payment import Payment

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        
        widgets = {
            "pay_date": forms.widgets.DateInput(attrs={"type": "date", "min": (timezone.now()).date()}),
        }

    def __init__(self,  *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"