# admin.py in myApp
from django.contrib import admin
from .models import HeroSection, Service

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


from .models import AboutSection

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')


from .models import BenefitsSection

@admin.register(BenefitsSection)
class BenefitsSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')


from .models import ContactImage

@admin.register(ContactImage)
class ContactImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text',)


from django.contrib import admin
from .models import FAQ, FAQSection, Service, ContactImage

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'order')
    search_fields = ('question',)
    ordering = ('order',)




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
