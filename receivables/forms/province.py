from django import forms
from django.utils import timezone
from django.forms import ModelForm
from receivables.models.province import Province

class ProvinceForm(ModelForm):
    class Meta:
        model = Province
        fields = "__all__"
        
    def __init__(self,  *args, **kwargs):
        super(ProvinceForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"