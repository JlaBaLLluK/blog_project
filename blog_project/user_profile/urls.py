from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from django.views.generic import TemplateView

from user_profile.views import SignupView, ProfileSettingsView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user_profile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/',
         login_required(TemplateView.as_view(template_name='user_profile/user_profile.html'), login_url='login'),
         name='profile'),
    path('profile/profile-settings/',
         login_required(ProfileSettingsView.as_view(template_name='user_profile/profile_settings.html'),
                        login_url='login'), name='profile_settings'),
]
