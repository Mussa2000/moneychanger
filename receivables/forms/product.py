from django import forms
from django.utils import timezone
from django.forms import ModelForm
from receivables.models.product import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self,  *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"