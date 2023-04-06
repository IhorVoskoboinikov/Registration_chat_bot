from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from registration.views import RegistrationView, ProfileView, CustomLoginView
from telegram_bot_registration import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
