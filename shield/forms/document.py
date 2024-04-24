from django import forms
from django.utils import timezone
from django.forms import ModelForm
from shield.models.document import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = "__all__"
        
        # widgets = {
        #     "deadline": forms.widgets.DateInput(attrs={"type": "date", "min": (timezone.now()).date()}),
        # }

    def __init__(self,  *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"