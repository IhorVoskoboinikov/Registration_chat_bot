from django.contrib import admin
from .models import ClientProfile


class ClientsProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'first_name', 'last_name', 'phone', 'photo', 'user')
    list_display_links = ('id', 'user_name')
    search_fields = ('id', 'first_name', 'last_name', 'phone', 'telegram_id')
    search_help_text = 'Search by first_name, last_name, phone'
    list_per_page = 25
    list_max_show_all = 100


admin.site.register(ClientProfile, ClientsProfileAdmin)

