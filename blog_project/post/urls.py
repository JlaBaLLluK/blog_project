from django.contrib.auth.decorators import login_required
from django.urls import path

from post.views import SinglePostView, WritePostView

urlpatterns = [
    path('write-post/', login_required(WritePostView.as_view(), login_url='login'), name='write_post'),
    path('<int:post_id>/', SinglePostView.as_view(), name='single_post')
]
