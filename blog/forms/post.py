from blog.models.post import Post
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

class PostForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'row bg-white'
        # self.helper.form_id = 'post-create-form-id'
        self.helper.layout = Layout(
            Row(
                Field('owner', css_class="col-md-6 col-lg-6 col-sm-6"),
                Field('category', css_class="col-md-6 col-lg-6 col-sm-6"),
            ),
            Row(
                Field('title', css_class="col-md-6 col-lg-6 col-sm-6"),
            ),
            Column(
                Field('body', css_class="col-md-12 col-sm-12"),
                Field('is_active', css_class="col-md-12 col-sm-12"),
            ),
            Div(
                Submit('submit', 'create post', css_class='btn btn-success w-100'),
                css_class='mt-2'
            ),
        )
    class Meta:
        model = Post
        fields = ['owner', 'title', 'category', 'body', 'is_active']

