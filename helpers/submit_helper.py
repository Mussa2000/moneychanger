from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SubmitButtonHelper:
    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
    helper.form_method = "POST"
