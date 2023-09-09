from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from post.forms import WritePostForm, DeletePostForm
from post.models import Post


class AllUserPostsView(View):
    template_name = 'post/all_posts.html'

    def get(self, request, username):
        posts = Post.objects.filter(author=request.user)
        return render(request, self.template_name, {'posts': posts})


class SinglePostView(View):
    template_name = 'post/single_post.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, self.template_name, {'post': post})


class AllPostsView(View):
    template_name = 'index.html'

    def get(self, request):
        posts = Post.objects.all().order_by('-publish_date')
        return render(request, self.template_name, {'posts': posts})


class WritePostView(View):
    template_name = 'post/write_post.html'

    def get(self, request):
        return render(request, self.template_name, {'form': WritePostForm})

    def post(self, request):
        form = WritePostForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        post_title = form.cleaned_data.get('post_title')
        post_text = form.cleaned_data.get('post_text')
        author = request.user
        post = Post(post_title=post_title, post_text=post_text, author=author)
        post.save()
        return redirect('profile', request.user.username)


class DeletePostView(View):
    template_name = 'post/delete_post.html'

    def get(self, request, post_id):
        return render(request, self.template_name, {'form': DeletePostForm})

    def post(self, request, post_id):
        form = DeletePostForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        password = form.cleaned_data.get('password')
        if not check_password(password, request.user.password):
            raise ValidationError("Password is wrong!")

        Post.objects.get(id=post_id).delete()

        return redirect('all_posts', request.user)
