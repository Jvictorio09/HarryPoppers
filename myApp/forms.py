from django import forms

class NewContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Full Name'
        }),
        label='Full Name',
        required=True
    )
    email_address = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Email Address'
        }),
        label='Email Address',
        required=True
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Phone Number'
        }),
        label='Phone Number',
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Your Message',
            'rows': 4
        }),
        label='Message',
        required=True
    )
    inquiry_type = forms.ChoiceField(
        choices=[
            ('General Inquiry', 'General Inquiry'),
            ('Support', 'Support')
        ],
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input'
        }),
        label='Inquiry Type',
        required=True
    )



from django import forms
from .models import (
    Product,
    HeroSection,
    Service,
    AboutSection,
    BenefitsSection,
    ContactImage,
    FAQ,
    FAQSection,
)


# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'secondary_image']


# Hero Section Form
class HeroSectionForm(forms.ModelForm):
    class Meta:
        model = HeroSection
        fields = ['title', 'subtitle', 'description', 'image', 'button_text', 'button_url']


# Service Form
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price', 'image', 'alt_text', 'link']


# About Section Form
class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = [
            'heading',
            'subheading',
            'description1',
            'description2',
            'description3',
            'image1',
            'image2',
            'image3',
        ]


# Benefits Section Form
class BenefitsSectionForm(forms.ModelForm):
    class Meta:
        model = BenefitsSection
        fields = [
            'heading',
            'subheading',
            'description',
            'benefit_1',
            'benefit_2',
            'benefit_3',
            'benefit_4',
            'image',
        ]


# Contact Image Form
class ContactImageForm(forms.ModelForm):
    class Meta:
        model = ContactImage
        fields = ['image', 'alt_text']


# FAQ Form
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'order', 'image']


# FAQ Section Form
class FAQSectionForm(forms.ModelForm):
    class Meta:
        model = FAQSection
        fields = ['title', 'description', 'side_image']
