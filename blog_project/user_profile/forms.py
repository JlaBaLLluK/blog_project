from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
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


class ResetPasswordForm(Form):
    username = CharField(max_length=30, required=True)
    new_password = CharField(widget=PasswordInput, min_length=8)
    repeat_password = CharField(widget=PasswordInput, min_length=8)

    def clean(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            raise ValidationError('This username is wrong!')

        new_password = self.cleaned_data.get('new_password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if new_password != repeat_password:
            raise ValidationError('Passwords are different!')

        return self.cleaned_data
