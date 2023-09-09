from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, CharField, PasswordInput

from post.models import Post


class WritePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("post_title", "post_text")


class DeletePostForm(Form):
    password = CharField(widget=PasswordInput, required=True)
    password_confirm = CharField(widget=PasswordInput, required=True)

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError("Passwords are different!")

        return self.cleaned_data
