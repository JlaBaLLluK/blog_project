from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import View


class SignupView(View):
    template_name = 'user_profile/signup.html'

    def get(self, request):
        return render(request, self.template_name, {'form': UserCreationForm})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(None, 'user_profile/registration_done.html', {'user': user})


class ProfileView(View):
    template_name = 'user_profile/user_profile.html'

    def get(self, request):
        return render(request, self.template_name)
