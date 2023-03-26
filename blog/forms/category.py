from blog.models.category import Category
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
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


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column(
                Field('name', css_class="col-md-12 col-sm-12"),
            ),
        )
        Div(
            Submit('submit', 'Add Category', css_class='btn btn-success w-100'),
            css_class='mt-2'
        ),

    
    class Meta:
        model = Category
        fields = [
            'name',
        ]
