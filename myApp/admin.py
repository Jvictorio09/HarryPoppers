# admin.py in myApp
from django.contrib import admin
from .models import HeroSection, Service

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')



from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    site_header = "Harry Poppers Admin"
    index_title = "Welcome to Your Admin Dashboard"

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_dashboard_url'] = reverse('admin_landing_page')
        return super().index(request, extra_context=extra_context)

# Replace the default admin site
admin_site = MyAdminSite(name='custom_admin')
