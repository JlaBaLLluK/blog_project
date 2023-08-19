from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from user_profile.forms import ChangeUsernameForm, ResetPasswordForm, SignupForm


class SignupView(View):
    template_name = 'user_profile/signup.html'

    def get(self, request):
        return render(request, self.template_name, {'form': SignupForm})

    def post(self, request):
        form = SignupForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(None, 'user_profile/registration_done.html', {'user': user})


class ProfileView(View):
    template_name = 'user_profile/user_profile.html'

    def get(self, request, username):
        if username != request.user.username:
            raise Http404

        return render(request, self.template_name)


class ChangeUsernameView(View):
    template_name = 'user_profile/change_username.html'

    def get(self, request, username):
        if username != request.user.username:
            raise Http404

        return render(request, self.template_name, {'form': ChangeUsernameForm})

    def post(self, request, username):
        form = ChangeUsernameForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        new_username = form.cleaned_data.get('new_username')
        password = form.cleaned_data.get('password')
        if not check_password(password, request.user.password):
            raise ValidationError("This password is wrong!")

        user = request.user
        user.username = new_username
        user.save()
        authenticate(username=new_username, password=password)
        return redirect('profile', new_username)


class ResetPasswordView(View):
    template_name = 'user_profile/password_reset.html'

    def get(self, request):
        return render(request, self.template_name, {'form': ResetPasswordForm})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        username = request.POST['username']
        new_password = form.cleaned_data.get('new_password')
        if check_password(new_password, request.user.password):
            raise ValidationError("The new password cannot be the same as the old password!")

        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        return render(None, 'user_profile/password_reset_done.html')
