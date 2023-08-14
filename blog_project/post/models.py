from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, TextField


class Post(models.Model):
    post_title = CharField(max_length=100, blank=False)
    post_text = TextField(blank=False)
    publish_date = DateTimeField(auto_now=True)
    author = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
