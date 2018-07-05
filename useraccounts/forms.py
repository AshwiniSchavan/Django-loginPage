from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30 ,required=False, help_text= ' Oprional')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optinal')
    # email_id = forms.EmailField(max_length=30, required=False, help_text='Optinal')
    # birth_date = forms.DateField(help_text='Resuired formate : YYYY-MM-DD')
    email = forms.EmailField(max_length=324, help_text='required. Conform valid email address')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
