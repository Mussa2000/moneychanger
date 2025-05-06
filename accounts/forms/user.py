from allauth.account.forms import SignupForm
from django import forms

from accounts.models.user import CustomUser, KYCProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    USER_ROLE_CHOICES = [
        ('Trader', 'Trader'),
        ('Regulator', 'Regulator'),
    ]
    user_role = forms.ChoiceField(choices=USER_ROLE_CHOICES, label='User Role', initial='Trader')
    profile_picture = forms.ImageField(required=False, label='Profile Picture')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.user_role= self.cleaned_data.get('user_role')
        if self.cleaned_data.get('profile_picture'):
            user.profile_picture = self.cleaned_data.get('profile_picture')
        user.save()
        return user
    
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)

from django.forms import ModelForm
class KYCProfileForm(ModelForm):
    class Meta:
        model = KYCProfile
        exclude = ['user']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={"type": "date"}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(KYCProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'