from django import forms
from django.forms import ModelForm
from .models import ChatMessage, Currency, ExchangeProposal, ExchangeSource, ExchangeRate, Transaction, UserExchangeRate

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

class UserExchangeRateForm(ModelForm):
    class Meta:
        model = UserExchangeRate
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={"type": "date"})
        }

    def __init__(self, *args, **kwargs):
        super(UserExchangeRateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
class ExchangeProposalForm(ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ['seller_rate', 'buyer', 'proposed_rate', 'amount', 'status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'proposed_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ExchangeProposalForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['proposal', 'sender', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(ChatMessageForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'