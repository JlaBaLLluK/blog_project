from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.forms import Form, CharField, PasswordInput, ModelForm


class SignupForm(ModelForm):
    password = CharField(widget=PasswordInput, min_length=8)
    password_confirm = CharField(widget=PasswordInput, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ['username', ]

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if len(User.objects.filter(username=username)) != 0:
            raise ValidationError("This username is already taken!")

        if ' ' in username:
            raise ValidationError("Username can't contain spaces!")

        if password.isnumeric():
            raise ValidationError("Password can't contain only digits!")

        if password != password_confirm:
            raise ValidationError("Passwords are different!")

        return self.cleaned_data


class ChangeUsernameForm(Form):
    new_username = CharField(max_length=30, required=True)
    password = CharField(widget=PasswordInput)

    def clean(self):
        new_username = self.cleaned_data.get('new_username')
        password = self.cleaned_data.get('password')
        if len(User.objects.filter(username=new_username)) != 0:
            raise ValidationError("This username is already taken!")

        if ' ' in new_username:
            raise ValidationError("Username can't contain spaces!")

        return self.cleaned_data


class ResetPasswordForm(Form):
    username = CharField(max_length=30, required=True)
    new_password = CharField(widget=PasswordInput, min_length=8)
    repeat_password = CharField(widget=PasswordInput, min_length=8)

    def clean(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            raise ValidationError('This username is wrong!')

        new_password = self.cleaned_data.get('new_password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if check_password(new_password, user.password):
            raise ValidationError("The new password cannot be the same as the old password!")

        if new_password != repeat_password:
            raise ValidationError('Passwords are different!')

        if new_password.isnumeric():
            raise ValidationError("Password can't contain only digits!")

        return self.cleaned_data
