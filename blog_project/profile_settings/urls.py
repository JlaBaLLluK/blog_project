from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from post.views import AllUserPostsView
from profile_settings.views import DeleteProfileView, ChangePasswordView, ChangeUsernameView, ResetPasswordView

urlpatterns = [
    path('all-posts/', login_required(AllUserPostsView.as_view(), login_url='login'), name='all_posts'),
    path('change-username/', login_required(ChangeUsernameView.as_view(), login_url='login'),
         name='change_username'),
    path('password-change/', login_required(ChangePasswordView.as_view(), login_url='login'),
         name='change_password'),
    path('delete_profile/', login_required(DeleteProfileView.as_view(), login_url='login'), name='profile_delete'),
    path('profile-settings/',
         login_required(TemplateView.as_view(template_name='profile_settings/profile_settings.html'),
                        login_url='login'), name='profile_settings'),
    path('password-reset/', ResetPasswordView.as_view(), name='reset_password'),
]
