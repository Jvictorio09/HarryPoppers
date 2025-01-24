from django.shortcuts import render

from django.shortcuts import render
from .models import HeroSection
from django.contrib.admin.views.decorators import staff_member_required


from django.shortcuts import render
from .models import HeroSection, Service, AboutSection, BenefitsSection, ContactImage, FAQ, FAQSection
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from .forms import NewContactForm  # Import the new contact form

def index(request):
    # Fetch static content for the page
    contact_images = ContactImage.objects.all()[:5]
    hero_section = HeroSection.objects.first()
    services = Service.objects.all()
    faqs = FAQ.objects.all()
    faq_section = FAQSection.objects.first()
    about_section = AboutSection.objects.first()
    benefits_section = BenefitsSection.objects.first()

    if request.method == 'POST':
        # Use the new contact form for validation
        form = NewContactForm(request.POST)
        if form.is_valid():
            # Get cleaned form data
            full_name = form.cleaned_data['full_name']
            email_address = form.cleaned_data['email_address']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            inquiry_type = form.cleaned_data['inquiry_type']

            # Prepare email context for admin
            admin_context = {
                'full_name': full_name,
                'email_address': email_address,
                'phone_number': phone_number,
                'message': message,
                'inquiry_type': inquiry_type
            }

            # Render email content
            admin_html_content = render_to_string('myApp/main/admin_email_template.html', admin_context)
            admin_text_content = strip_tags(admin_html_content)

            # Send email to admin
            admin_email = EmailMultiAlternatives(
                subject=f"New {inquiry_type} from {full_name}",
                body=admin_text_content,
                from_email='harrypopperstore@gmail.com',
                to=['harrypopperstore@gmail.com']
            )
            admin_email.attach_alternative(admin_html_content, "text/html")
            admin_email.send()

            send_confirmation_email(full_name, email_address)
            print(f"Sending confirmation email to {email_address}")


            # Optionally redirect to a success page
            return redirect('index')  # Replace 'index' with a success page if needed
        else:
            # If form is invalid, render the page with error messages
            return render(request, 'myApp/main/index.html', {
                'hero_section': hero_section,
                'services': services,
                'about_section': about_section,
                'benefits_section': benefits_section,
                'contact_images': contact_images,
                'faqs': faqs,
                'faq_section': faq_section,
                'form': form,  # Pass the form with errors
            })

    # For GET requests, initialize the form
    form = NewContactForm()

    return render(request, 'myApp/main/index.html', {
        'hero_section': hero_section,
        'services': services,
        'about_section': about_section,
        'benefits_section': benefits_section,
        'contact_images': contact_images,
        'faqs': faqs,
        'faq_section': faq_section,
        'form': form,  # Pass the new contact form to the template
    })


     


def send_confirmation_email(name, email):
    subject = "Thank You for Your Inquiry"
    message = render_to_string('myApp/main/confirmation_email_template.html', {'name': name})
    plain_message = strip_tags(message)
    
    confirmation_email = EmailMultiAlternatives(
        subject,
        plain_message,
        'harrypopperstore@gmail.com',
        [email]
    )
    
    confirmation_email.attach_alternative(message, "text/html")
    confirmation_email.send()



from django.shortcuts import render, redirect
from django.core.mail import send_mail
  
from .models import ContactImage
from django.http import JsonResponse

from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import NewContactForm

def new_contact_view(request):
    if request.method == 'POST':
        form = NewContactForm(request.POST)
        if form.is_valid():
            # Handle form data
            full_name = form.cleaned_data['full_name']
            email_address = form.cleaned_data['email_address']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            inquiry_type = form.cleaned_data['inquiry_type']

            # Optionally send email or save to database
            # Example: Send email
            subject = f"New {inquiry_type} from {full_name}"
            body = f"""
            Name: {full_name}
            Email: {email_address}
            Phone: {phone_number}
            Message: {message}
            Inquiry Type: {inquiry_type}
            """
            send_mail(subject, body, 'harrypopperstore@gmail.com')  

            return JsonResponse({'status': 'success', 'message': 'Thank you for contacting us!'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data.'}, status=400)

    return render(request, 'new_contact_form.html', {'form': NewContactForm()})


from .models import AboutSection

from .models import HeroSection, AboutSection, BenefitsSection, Service, ContactImage, FAQ, FAQSection
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_landing_page(request):
    # Fetch the HeroSection, AboutSection, and BenefitsSection objects or create them if they don't exist
    hero_section = HeroSection.objects.first()
    about_section = AboutSection.objects.first()
    benefits_section = BenefitsSection.objects.first()
    contact_images = ContactImage.objects.all()
    faq_section = FAQSection.objects.first()
    faqs = FAQ.objects.all()

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
    if request.method == 'POST' and 'update_faq_section' in request.POST:
        faq_section.title = request.POST.get('faq_section_title', faq_section.title)
        faq_section.description = request.POST.get('faq_section_description', faq_section.description)
        if request.FILES.get('faq_section_image'):
            faq_section.side_image = request.FILES['faq_section_image']
        faq_section.save()

    # Handle FAQ items updates
    if request.method == 'POST' and 'update_faq_items' in request.POST:
        for faq_id in request.POST.getlist('faq_ids'):
            faq = FAQ.objects.get(id=faq_id)
            faq.question = request.POST.get(f'faq_question_{faq_id}', faq.question)
            faq.answer = request.POST.get(f'faq_answer_{faq_id}', faq.answer)
            faq.order = request.POST.get(f'faq_order_{faq_id}', faq.order)
            if f'faq_image_{faq_id}' in request.FILES:
                faq.image = request.FILES[f'faq_image_{faq_id}']
            faq.save()
        

    # Context for the template
    context = {
        'hero_section': hero_section,
        'about_section': about_section,
        'benefits_section': benefits_section,
        'services': Service.objects.all(),
        'contact_images': contact_images,
        'faq_section': faq_section,
        'faqs': faqs,
    }
    return render(request, 'myApp/customadmin/custom_admin_dashboard.html', context)



