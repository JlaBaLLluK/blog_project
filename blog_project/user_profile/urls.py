from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from user_profile.views import SignupView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user_profile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', login_required(ProfileView.as_view(), login_url='login'), name='profile')
]
