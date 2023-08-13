from django.urls import path
from django.views.generic import TemplateView

from post.views import AllPostsView, SinglePostView

urlpatterns = [
    path('all-posts/', AllPostsView.as_view(), name='all_posts'),
    path('write-post/', TemplateView.as_view(template_name='post/write_post.html'), name='write_post'),
    path('<int:post_id>/', SinglePostView.as_view(), name='single_post')
]
