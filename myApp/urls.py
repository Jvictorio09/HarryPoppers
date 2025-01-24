from . import views
from django.urls import path

urlpatterns = [
     path("", views.index, name='index'),
     path('contact/', views.new_contact_view, name='contact'),
     path('customadmin/', views.admin_landing_page, name='admin_landing_page'),
      
]

