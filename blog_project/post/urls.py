from django.contrib.auth.decorators import login_required
from django.urls import path

from post.views import AllUserPostsView, SinglePostView, WritePostView

urlpatterns = [
    path('all-user-posts/', login_required(AllUserPostsView.as_view(), login_url='login'), name='all_posts'),
    path('write-post/', login_required(WritePostView.as_view(), login_url='login'), name='write_post'),
    path('<int:post_id>/', login_required(SinglePostView.as_view(), login_url='login'), name='single_post')
]
