from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path("contact/", views.new_contact_view, name="contact"), 
    path("harrypoppers/checkout/", views.checkout, name="checkout"), 
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
]
