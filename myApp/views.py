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

from django.shortcuts import render
from .models import HeroSection, AboutSection, BenefitsSection, Service, ContactImage, FAQ

@staff_member_required
def admin_landing_page(request):
    # Fetching data from the database
    hero_section = HeroSection.objects.first()
    about_section = AboutSection.objects.first()
    benefits_section = BenefitsSection.objects.first()
    products_count = Service.objects.count()  # Counting products
    contact_images_count = ContactImage.objects.count()  # Counting contact images
    faqs_count = FAQ.objects.count()  # Counting FAQs

    # Passing data to the template
    context = {
        'hero_section': hero_section,
        'about_section': about_section,
        'benefits_section': benefits_section,
        'products_count': products_count,
        'contact_images_count': contact_images_count,
        'faqs_count': faqs_count,
    }

    return render(request, 'myApp/customadmin/custom_admin_dashboard.html', context)

from django.shortcuts import redirect

from django.shortcuts import redirect

def redirect_to_custom_admin(request):
    return redirect('custom_admin:admin_landing_page')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import (
    Product, HeroSection, Service, AboutSection, BenefitsSection, ContactImage, FAQ, FAQSection
)
from .forms import (
    ProductForm, HeroSectionForm, ServiceForm, AboutSectionForm,
    BenefitsSectionForm, ContactImageForm, FAQForm, FAQSectionForm
)


# Common utility function for rendering modals
def render_modal_form(request, template_name, form, context=None):
    if context is None:
        context = {}
    context['form'] = form
    return render(request, template_name, context)


# ----------- Hero Section -----------
@staff_member_required
def hero_section(request):
    # Fetch the Hero Section or create a default one
    hero_section = HeroSection.objects.first()
    if not hero_section:
        hero_section = HeroSection.objects.create(
            title="Default Title",
            subtitle="Default Subtitle",
            description="Default Description"
        )

    # Handle form submission
    if request.method == 'POST' and 'update_hero' in request.POST:
        hero_section.title = request.POST.get('title', hero_section.title)
        hero_section.subtitle = request.POST.get('subtitle', hero_section.subtitle)
        hero_section.description = request.POST.get('description', hero_section.description)
        if request.FILES.get('image'):
            hero_section.image = request.FILES['image']
        hero_section.save()
        return redirect('custom_admin:hero_section')  # Reload the page to show updated data

    # Render the template
    return render(request, 'myApp/customadmin/partials/hero_section.html', {
        'hero_section': hero_section
    })


# ----------- Products (Add/Edit/Delete) -----------
from django.shortcuts import get_object_or_404, redirect, render
from .models import Service  # Still referring to the model as "Service"
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def products(request):
    # Fetch all services, alias as products for the frontend
    products = Service.objects.all()
    return render(request, 'myApp/customadmin/partials/products.html', {
        'products': products  # Alias services as products in the context
    })


@staff_member_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        alt_text = request.POST.get('alt_text', '')
        link = request.POST.get('link', '#')
        description = request.POST.get('description', '')

        Service.objects.create(
            name=name,
            price=price,
            image=image,
            alt_text=alt_text,
            link=link,
            description=description
        )
        return redirect('custom_admin:products')

    return render(request, 'myApp/customadmin/partials/add_product_modal.html')


@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Service, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name', product.name)
        product.price = request.POST.get('price', product.price)
        product.alt_text = request.POST.get('alt_text', product.alt_text)
        product.link = request.POST.get('link', product.link)
        product.description = request.POST.get('description', product.description)
        if request.FILES.get('image'):
            product.image = request.FILES['image']
        product.save()
        return redirect('custom_admin:products')

    return render(request, 'myApp/customadmin/partials/edit_product_modal.html', {
        'product': product
    })


@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Service, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('custom_admin:products')

    return render(request, 'myApp/customadmin/partials/delete_product_modal.html', {
        'product': product
    })

# ----------- Other Views for About Section, Benefits Section, etc. -----------

@staff_member_required
def about_section(request):
    # Fetch the About Section or create a default one
    about_section = AboutSection.objects.first()
    if not about_section:
        about_section = AboutSection.objects.create(
            heading="Default Heading",
            subheading="Default Subheading",
            description1="Default Description 1",
            description2="Default Description 2",
            description3="Default Description 3"
        )

    # Handle form submission
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
        return redirect('custom_admin:about_section')  # Reload the page to show updated data

    # Render the template
    return render(request, 'myApp/customadmin/partials/about_section.html', {
        'about_section': about_section
    })



from django.shortcuts import render, get_object_or_404, redirect
from .models import BenefitsSection
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def benefits_section(request):
    # Fetch the BenefitsSection instance (assuming there's only one)
    benefits_section = BenefitsSection.objects.first()

    # If POST request, handle updates
    if request.method == 'POST':
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
        return redirect('custom_admin:benefits_section')

    return render(request, 'myApp/customadmin/partials/benefits_section.html', {
        'benefits_section': benefits_section,
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactImage
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def contact_images(request):
    # Fetch all contact images
    contact_images = ContactImage.objects.all()

    if request.method == 'POST' and 'add_image' in request.POST:
        # Add new contact image
        image = request.FILES.get('image')
        alt_text = request.POST.get('alt_text', 'Default Alt Text')
        ContactImage.objects.create(image=image, alt_text=alt_text)
        return redirect('custom_admin:contact_images')

    return render(request, 'myApp/customadmin/partials/contact_images.html', {
        'contact_images': contact_images,
    })

@staff_member_required
def edit_contact_image(request, image_id):
    contact_image = get_object_or_404(ContactImage, id=image_id)
    if request.method == 'POST':
        contact_image.alt_text = request.POST.get('alt_text', contact_image.alt_text)
        if request.FILES.get('image'):
            contact_image.image = request.FILES['image']
        contact_image.save()
        return redirect('custom_admin:contact_images')
    return render(request, 'myApp/customadmin/partials/edit_contact_image_modal.html', {
        'contact_image': contact_image,
    })

@staff_member_required
def delete_contact_image(request, image_id):
    contact_image = get_object_or_404(ContactImage, id=image_id)
    if request.method == 'POST':
        contact_image.delete()
        return redirect('custom_admin:contact_images')


def faqs(request):
    faqs = FAQ.objects.all()
    faq_section = FAQSection.objects.first()

    if request.method == 'POST':
        form = FAQForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})

    context = {'faqs': faqs, 'faq_section': faq_section, 'form': FAQForm()}
    return render(request, 'myApp/customadmin/partials/faqs.html', context)
