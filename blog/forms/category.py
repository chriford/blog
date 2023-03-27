from blog.models.category import Category
from django.forms import ModelForm
from django.urls import reverse_lazy
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
        self.helper.form_action = ''
        self.helper.form_method = ''
        self.helper.layout = Layout(
            HTML("{% csrf_token %}"),
            Column(
                Field('name', css_class="col-md-12 col-sm-12"),
            ),
            Submit('submit', 'Add Category', css_class='btn btn-success w-100 mt-2'),   
        )
    
    class Meta:
        model = Category
        fields = [
            'name',
        ]
