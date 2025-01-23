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
