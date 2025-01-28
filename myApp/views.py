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


from django.shortcuts import render, get_object_or_404
from .models import Service

def product_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, "myApp/main/product_detail.html", {"service": service})



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
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from .models import HeroSection, AboutSection, BenefitsSection, Service, ContactImage, FAQ, FAQSection
from .forms import FAQForm


# Custom decorator to check if the user is staff
def staff_required(view_func):
    @user_passes_test(lambda u: u.is_authenticated and u.is_staff, login_url="custom_admin:login")
    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)
    return wrapped_view


# Admin Login View
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("custom_admin:admin_landing_page")
        else:
            return render(request, "myApp/customadmin/login.html", {"error": "Invalid credentials or not a staff member."})
    return render(request, "myApp/customadmin/login.html")


# Admin Logout View
@login_required(login_url="custom_admin:login")
def admin_logout(request):
    logout(request)
    return redirect("custom_admin:login")

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = "myApp/customadmin/login.html"  # Path to your login template
    redirect_authenticated_user = True
    next_page = reverse_lazy("custom_admin:admin_landing_page")


@login_required
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
@login_required
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

@login_required
def products(request):
    # Fetch all services, alias as products for the frontend
    products = Service.objects.all()
    return render(request, 'myApp/customadmin/partials/products.html', {
        'products': products  # Alias services as products in the context
    })


@login_required
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


@login_required
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


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Service, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('custom_admin:products')

    return render(request, 'myApp/customadmin/partials/delete_product_modal.html', {
        'product': product
    })

# ----------- Other Views for About Section, Benefits Section, etc. -----------

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def delete_contact_image(request, image_id):
    contact_image = get_object_or_404(ContactImage, id=image_id)
    if request.method == 'POST':
        contact_image.delete()
        return redirect('custom_admin:contact_images')


from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import FAQ, FAQSection
from .forms import FAQForm, FAQSectionForm  # Ensure FAQSectionForm is created for handling FAQSection data
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import FAQ, FAQSection
from .forms import FAQForm, FAQSectionForm


def manage_faqs(request):
    faqs = FAQ.objects.all()  # Retrieve all FAQs
    faq_section = FAQSection.objects.first()  # Retrieve the FAQ Section (only one expected)

    # Create default forms
    faq_form = FAQForm()  # For adding a new FAQ
    faq_section_form = FAQSectionForm(instance=faq_section)  # For editing the FAQ Section
    faq_forms = {faq.id: FAQForm(instance=faq) for faq in faqs}  # Forms for editing each FAQ

    if request.method == 'POST':
        # Add a new FAQ
        if 'add_faq' in request.POST:
            faq_form = FAQForm(request.POST, request.FILES)
            if faq_form.is_valid():
                faq_form.save()
                messages.success(request, "FAQ added successfully!")
                return redirect('custom_admin:manage_faqs')

        # Edit an existing FAQ
        elif 'edit_faq' in request.POST:
            faq_id = request.POST.get('faq_id')
            faq = get_object_or_404(FAQ, id=faq_id)
            faq_form = FAQForm(request.POST, request.FILES, instance=faq)
            if faq_form.is_valid():
                faq_form.save()
                messages.success(request, "FAQ updated successfully!")
                return redirect('custom_admin:manage_faqs')

        # Delete an FAQ
        elif 'delete_faq' in request.POST:
            faq_id = request.POST.get('faq_id')
            faq = get_object_or_404(FAQ, id=faq_id)
            faq.delete()
            messages.success(request, "FAQ deleted successfully!")
            return redirect('custom_admin:manage_faqs')

        # Edit the FAQ Section
        elif 'edit_faq_section' in request.POST:
            faq_section_form = FAQSectionForm(request.POST, request.FILES, instance=faq_section)
            if faq_section_form.is_valid():
                faq_section_form.save()
                messages.success(request, "FAQ Section updated successfully!")
                return redirect('custom_admin:manage_faqs')

    # Context data for the template
    context = {
        'faqs': faqs,
        'faq_section': faq_section,
        'faq_form': faq_form,
        'faq_section_form': faq_section_form,
        'faq_forms': faq_forms,  # Include forms for each FAQ
    }
    return render(request, 'myApp/customadmin/partials/faq_section.html', context)

 

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_user_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'User with this email already exists.'}, status=400)

        # Generate a random temporary password
        temporary_password = get_random_string(8)

        # Create the user
        user = User.objects.create_user(
            username=email,  # Set email as the username
            email=email,
            password=temporary_password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True  # Grant staff access (optional)
        user.save()

        # Send email to the user
        subject = "Access Granted: Temporary Password"
        message = f"""
        Hi {first_name},

        Your access to the admin dashboard has been created. Below are your credentials:

        Username: {email}
        Temporary Password: {temporary_password}

        Please log in and update your password immediately.

        Regards,
        Admin Team
        """
        send_mail(
            subject,
            message,
            'harrypopperstore@gmail.com',  # Replace with your email
            [email],
            fail_silently=False,
        )

        return JsonResponse({'status': 'success', 'message': 'User profile created and email sent.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)  # Keep the user logged in after password change
            return JsonResponse({'status': 'success', 'message': 'Password updated successfully!'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

