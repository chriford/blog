from blog.models.image import Image
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy
from crispy_forms.layout import (
    Layout,
    Div,
    Row,
    Column,
    Field,
    Submit,
    HTML,
    Fieldset,
)


class ImageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                """{% csrf_token %}
            <p class='text-center border-bottom py-2 text-muted'>create your new blog here</p>
            <h /r>"""
            ),
            Row(
                Field("post", css_class="col-md-6 col-lg-6 col-sm-6"),
                Field("file", css_class="col-md-6 col-lg-6 col-sm-6"),
            ),
            Div(
                Submit("submit", "Attach file", css_class="btn btn-success w-100"),
                css_class="mt-2",
            ),
        )

    class Meta:
        model = Image
        fields = ["post", "file"]
