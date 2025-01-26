from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import (
    HeroSection,
     
    AboutSection,
    BenefitsSection,
    ContactImage,
    FAQ,
    FAQSection,
)


# Register models with the custom admin site
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


 

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')


@admin.register(BenefitsSection)
class BenefitsSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')


@admin.register(ContactImage)
class ContactImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'order')
    search_fields = ('question',)
    ordering = ('order',)
