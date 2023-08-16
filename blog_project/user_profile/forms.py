from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, PasswordInput


class ChangeUsernameForm(Form):
    new_username = CharField(max_length=30, required=True)
    password = CharField(widget=PasswordInput)

    def clean(self):
        new_username = self.cleaned_data.get('new_username')
        password = self.cleaned_data.get('password')
        old_user = User.objects.filter(username=new_username)
        if len(old_user) != 0:
            raise ValidationError('This username is already taken!')

        return self.cleaned_data
