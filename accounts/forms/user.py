from allauth.account.forms import SignupForm
from django import forms
from receivables.models.province import Province


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    province = forms.ModelChoiceField(queryset=Province.objects.all(), required=False, label='Province')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.province = self.cleaned_data.get('province')
        user.save()
        return user