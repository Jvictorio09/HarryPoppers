from django.core.management.base import BaseCommand
from myApp.models import Service
from django.utils.text import slugify

class Command(BaseCommand):
    help = "Generate slugs for existing products without slugs"

    def handle(self, *args, **kwargs):
        services = Service.objects.filter(slug__isnull=True)
        for service in services:
            service.slug = slugify(service.name)
            service.save()
            self.stdout.write(f"Slug generated for: {service.name}")
        self.stdout.write(self.style.SUCCESS("All missing slugs have been generated."))
