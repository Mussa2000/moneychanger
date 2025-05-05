from django import forms
from django.forms import ModelForm
from .models import Currency, ExchangeSource, ExchangeRate, Transaction

class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ExchangeSourceForm(ModelForm):
    class Meta:
        model = ExchangeSource
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ExchangeSourceForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ExchangeRateForm(ModelForm):
    class Meta:
        model = ExchangeRate
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={"type": "date"})
        }

    def __init__(self, *args, **kwargs):
        super(ExchangeRateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'