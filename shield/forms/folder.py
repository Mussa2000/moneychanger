from django import forms
from django.utils import timezone
from django.forms import ModelForm
from shield.models.folder import Folder

class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = "__all__"
        
        # widgets = {
        #     "deadline": forms.widgets.DateInput(attrs={"type": "date", "min": (timezone.now()).date()}),
        # }

    def __init__(self,  *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"