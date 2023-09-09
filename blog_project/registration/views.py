from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from registration.forms import SignupForm


class SignupView(View):
    template_name = 'registration/signup.html'

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
        return render(None, 'registration/registration_done.html', {'user': user})
