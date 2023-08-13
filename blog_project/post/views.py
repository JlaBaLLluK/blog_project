from django.shortcuts import render
from django.views import View

from post.models import Post


class AllPostsView(View):
    template_name = 'post/all_posts.html'

    def get(self, request):
        posts = Post.objects.filter(author=request.user)
        return render(request, self.template_name, {'posts': posts})


class SinglePostView(View):
    template_name = 'post/single_post.html'

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        return render(request, self.template_name, {'post': post})
