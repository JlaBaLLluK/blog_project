from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from profile_settings.forms import ChangeUsernameForm, ChangePasswordForm, ResetPasswordForm, DeleteProfileForm


class ChangeUsernameView(View):
    template_name = 'profile_settings/change_username.html'

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


class ChangePasswordView(View):
    template_name = 'profile_settings/password_change.html'

    def get(self, request, username):
        return render(request, self.template_name, {'form': ChangePasswordForm})

    def post(self, request, username):
        form = ChangePasswordForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        old_password = form.cleaned_data.get('old_password')
        new_password = form.cleaned_data.get('new_password')
        new_password_confirm = form.cleaned_data.get('new_password_confirm')
        if not check_password(old_password, request.user.password):
            raise ValidationError("Old password is wrong!")

        request.user.set_password(new_password)
        request.user.save()
        login(request, request.user)
        return render(None, 'profile_settings/password_change_done.html', {'username': username})


class ResetPasswordView(View):
    template_name = 'profile_settings/password_reset.html'

    def get(self, request):
        return render(request, self.template_name, {'form': ResetPasswordForm})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        username = request.POST['username']
        new_password = form.cleaned_data.get('new_password')
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        return render(None, 'profile_settings/password_reset_done.html')


class DeleteProfileView(View):
    template_name = 'profile_settings/delete_profile.html'

    def get(self, request, username):
        return render(request, self.template_name, {'form': DeleteProfileForm})

    def post(self, request, username):
        form = DeleteProfileForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        password = form.cleaned_data.get('password')
        if not check_password(password, request.user.password):
            raise ValidationError("Password is wrong!")

        User.objects.get(username=username).delete()
        return redirect('homepage')
