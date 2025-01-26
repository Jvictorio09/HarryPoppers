from django.urls import path
from myApp import views

app_name = 'custom_admin'  # Namespace for custom admin URLs

urlpatterns = [
    path('', views.admin_landing_page, name='admin_landing_page'),  # Custom admin homepage
    path('hero-section/', views.hero_section, name='hero_section'),
    path('about-section/', views.about_section, name='about_section'),
    path('products/', views.products, name='products'),
    path('products/add/', views.add_product, name='add_product'),  # Add product URL
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),  # Edit product URL
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),  # Delete product URL
    path('benefits-section/', views.benefits_section, name='benefits_section'),
    path('contact-images/', views.contact_images, name='contact_images'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact-images/', views.contact_images, name='contact_images'),
    path('contact-images/edit/<int:image_id>/', views.edit_contact_image, name='edit_contact_image'),
    path('contact-images/delete/<int:image_id>/', views.delete_contact_image, name='delete_contact_image'),

]
