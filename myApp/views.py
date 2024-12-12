from django.shortcuts import render

from django.shortcuts import render
from .models import HeroSection
from django.contrib.admin.views.decorators import staff_member_required


from django.shortcuts import render
from .models import HeroSection, Service, AboutSection, BenefitsSection, ContactImage

def index(request):
    contact_images = ContactImage.objects.all()[:5]
    hero_section = HeroSection.objects.first()  # Fetch the hero section
    services = Service.objects.all()
    about_section = AboutSection.objects.first()
    benefits_section = BenefitsSection.objects.first()
    return render(request, 'myApp/main/index.html', {
        'hero_section': hero_section,
        'services': services,
        'about_section': about_section,
        'benefits_section': benefits_section,
        'contact_images': contact_images
    })


from .models import AboutSection

from .models import HeroSection, AboutSection, BenefitsSection, Service, ContactImage
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_landing_page(request):
    # Fetch the HeroSection, AboutSection, and BenefitsSection objects or create them if they don't exist
    hero_section = HeroSection.objects.first()
    about_section = AboutSection.objects.first()
    benefits_section = BenefitsSection.objects.first()
    contact_images = ContactImage.objects.all()

    if not hero_section:
        hero_section = HeroSection.objects.create(
            title="Default Title",
            subtitle="Default Subtitle",
            description="Default description text"
        )
    
    if not about_section:
        about_section = AboutSection.objects.create(
            heading="Default Heading",
            subheading="Default Subheading",
            description1="Default Description 1",
            description2="Default Description 2",
            description3="Default Description 3"
        )
    
    if not benefits_section:
        benefits_section = BenefitsSection.objects.create(
            heading="Default Benefits Heading",
            subheading="Default Benefits Subheading",
            description="Default description for benefits",
            benefit_1="Default Benefit 1",
            benefit_2="Default Benefit 2",
            benefit_3="Default Benefit 3",
            benefit_4="Default Benefit 4"
        )
    
    # Handle HeroSection updates
    if request.method == 'POST' and 'update_hero' in request.POST:
        hero_section.title = request.POST.get('title', hero_section.title)
        hero_section.subtitle = request.POST.get('subtitle', hero_section.subtitle)
        hero_section.description = request.POST.get('description', hero_section.description)
        if request.FILES.get('image'):
            hero_section.image = request.FILES['image']
        hero_section.save()
    
    # Handle AboutSection updates
    if request.method == 'POST' and 'update_about' in request.POST:
        about_section.heading = request.POST.get('heading', about_section.heading)
        about_section.subheading = request.POST.get('subheading', about_section.subheading)
        about_section.description1 = request.POST.get('description1', about_section.description1)
        about_section.description2 = request.POST.get('description2', about_section.description2)
        about_section.description3 = request.POST.get('description3', about_section.description3)
        if request.FILES.get('image1'):
            about_section.image1 = request.FILES['image1']
        if request.FILES.get('image2'):
            about_section.image2 = request.FILES['image2']
        if request.FILES.get('image3'):
            about_section.image3 = request.FILES['image3']
        about_section.save()
    
    # Handle BenefitsSection updates
    if request.method == 'POST' and 'update_benefits' in request.POST:
        benefits_section.heading = request.POST.get('heading', benefits_section.heading)
        benefits_section.subheading = request.POST.get('subheading', benefits_section.subheading)
        benefits_section.description = request.POST.get('description', benefits_section.description)
        benefits_section.benefit_1 = request.POST.get('benefit_1', benefits_section.benefit_1)
        benefits_section.benefit_2 = request.POST.get('benefit_2', benefits_section.benefit_2)
        benefits_section.benefit_3 = request.POST.get('benefit_3', benefits_section.benefit_3)
        benefits_section.benefit_4 = request.POST.get('benefit_4', benefits_section.benefit_4)
        if request.FILES.get('image'):
            benefits_section.image = request.FILES['image']
        benefits_section.save()

        contact_images = ContactImage.objects.all()

    # Handle form submission for ContactImage updates
    if request.method == 'POST' and 'update_contact_images' in request.POST:
        for image_id in request.POST.getlist('image_ids'):
            image_obj = ContactImage.objects.get(id=image_id)
            if f'image_{image_id}' in request.FILES:
                image_obj.image = request.FILES[f'image_{image_id}']
            image_obj.alt_text = request.POST.get(f'alt_text_{image_id}', image_obj.alt_text)
            image_obj.save()
        

    # Context for the template
    context = {
        'hero_section': hero_section,
        'about_section': about_section,
        'benefits_section': benefits_section,
        'services': Service.objects.all(),
        'contact_images': contact_images,
    }
    return render(request, 'myApp/customadmin/custom_admin_dashboard.html', context)
