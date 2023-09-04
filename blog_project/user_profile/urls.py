from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.urls import path, include
from django.views.generic import TemplateView

from post.views import AllUserPostsView
from profile_settings.views import ChangeUsernameView, ChangePasswordView, ResetPasswordView, DeleteProfileView
from registration.views import SignupView
from user_profile.views import ProfileView

urlpatterns = [
    path('', include('login.urls')),
    path('', include('registration.urls')),
    path('<str:username>/', include('profile_settings.urls')),
    path('<str:username>/',
         login_required(ProfileView.as_view(), login_url='login'),
         name='profile'),
]
