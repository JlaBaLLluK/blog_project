from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.urls import path
from django.views.generic import TemplateView

from post.views import AllUserPostsView
from user_profile.views import SignupView, ProfileView, ChangeUsernameView, ResetPasswordView, ChangePasswordView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user_profile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('<str:username>/',
         login_required(ProfileView.as_view(), login_url='login'),
         name='profile'),
    path('profile/profile-settings/',
         login_required(TemplateView.as_view(template_name='user_profile/profile_settings.html'),
                        login_url='login'), name='profile_settings'),
    path('<str:username>/all-posts/', login_required(AllUserPostsView.as_view(), login_url='login'), name='all_posts'),
    path('<str:username>/change-username/', login_required(ChangeUsernameView.as_view(), login_url='login'),
         name='change_username'),
    path('<str:username>/password-change/', login_required(ChangePasswordView.as_view(), login_url='login'),
         name='change_password'),
    path('forgot-password/password-reset/', ResetPasswordView.as_view(), name='reset_password'),
]
