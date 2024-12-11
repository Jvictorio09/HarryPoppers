from django.shortcuts import render

from django.shortcuts import render
from .models import HeroSection
from django.contrib.admin.views.decorators import staff_member_required


from django.shortcuts import render
from .models import HeroSection, Service

def index(request):
    hero_section = HeroSection.objects.first()  # Fetch the hero section
    services = Service.objects.all()  # Fetch all services
    return render(request, 'myApp/main/index.html', {
        'hero_section': hero_section,
        'services': services
    })

from django.shortcuts import render, redirect
from .models import HeroSection, Service
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import HeroSection, Service

@staff_member_required
def admin_landing_page(request):
    # Get the first HeroSection object or create one if it doesn't exist
    hero_section = HeroSection.objects.first()
    services = Service.objects.all()
    if not hero_section:
        hero_section = HeroSection.objects.create(
            subtitle="Default Subtitle",
            title="Default Title",
            description="Default description text",
            button_text="Shop Now",
            button_url="#",
            image=None  # Set a placeholder image or leave as None
        )

    # Handle form submission for HeroSection updates
    if request.method == 'POST' and 'update_hero' in request.POST:
        hero_section.title = request.POST.get('title', hero_section.title)
        hero_section.subtitle = request.POST.get('subtitle', hero_section.subtitle)
        hero_section.description = request.POST.get('description', hero_section.description)
        if request.FILES.get('image'):
            hero_section.image = request.FILES['image']
        hero_section.save()
        return redirect('admin_landing_page')

    context = {
        'hero_section': hero_section,
        'services': services,
    }
    return render(request, 'myApp/customadmin/custom_admin_dashboard.html', context)
