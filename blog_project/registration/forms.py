from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput


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

        if password != password_confirm:
            raise ValidationError("Passwords are different!")

        if password.isnumeric():
            raise ValidationError("Password can't contain only digits!")

        return self.cleaned_data
