from django.http import Http404
from django.shortcuts import render
from django.views import View


class ProfileView(View):
    template_name = 'user_profile/user_profile.html'

    def get(self, request, username):
        if username != request.user.username:
            raise Http404

        return render(request, self.template_name)
