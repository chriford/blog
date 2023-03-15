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
        self.helper.form_class = ''
        self.helper.form_id = 'post-create-form-id'
        self.helper.layout = Layout(
            Column('body', css_class="col-md-12 col-md-12 col-12 col-sm-12"),
            Row(
                Field('title', css_class="col-md-6 col-lg-6 col-sm-6"),
                Field('category', css_class="col-md-6 col-lg-6 col-sm-6"),
            ),
            Column('body', css_class="col-md-12 col-sm-12"),
            Div(
                Submit('submit', 'create post', 
                    css_class='btn btn-success d-flex w-100 justify-content-center',
                    css_id="post-create-id",
                ),
                css_class="d-flex justify-content-center py-0 pb-1",
            )
        )

    class Meta:
        model = Post
        fields = ['owner', 'title', 'category', 'body',]

