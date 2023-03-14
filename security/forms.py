from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Div,
    Submit,
    HTML,
    Row,
    Column,
)
from security.models import User

class UserCreationForm(forms.Form):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit('submit', 'create user', css_class='btn btn-primary'),
        )
            
    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit=False)
        user = self.cleaned_data['email']
        if commit:
            user.save()
        return user