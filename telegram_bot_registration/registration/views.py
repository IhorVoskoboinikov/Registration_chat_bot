from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.views import LoginView
from django.urls import reverse

from registration.models import ClientProfile


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/profile/'

    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})


class ProfileView(View):
    def get(self, request, user_id):
        try:
            client_profile = ClientProfile.objects.get(user=user_id)
            user_data = {
                "user_name": client_profile.user_name,
                "first_name": client_profile.first_name,
                "last_name": client_profile.last_name,
                "phone": client_profile.phone,
                "photo": client_profile.photo if client_profile.photo else None,
            }
            print(user_data)
            return render(request, 'profile.html', {'user': user_data})
        except ClientProfile.DoesNotExist:
            # handle client profile not found
            pass


class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration.html')
