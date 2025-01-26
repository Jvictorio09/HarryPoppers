from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path("contact/", views.new_contact_view, name="contact"),  # Contact page
]
