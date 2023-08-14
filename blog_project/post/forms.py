from django.forms import ModelForm

from post.models import Post


class WritePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("post_title", "post_text")
