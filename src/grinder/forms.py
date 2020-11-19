from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        def __init__(self, *args, **kwargs):
            super(AbstractUserCreationForm, self).__init__(*args, **kwargs)
            ## add a "form-control" class to each form input
            ## for enabling bootstrap
            for name in self.fields.keys():
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        def __init__(self, *args, **kwargs):
            super(AbstractUserCreationForm, self).__init__(*args, **kwargs)
            ## add a "form-control" class to each form input
            ## for enabling bootstrap
            for name in self.fields.keys():
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })
