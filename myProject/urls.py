from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from myApp import views  # Import views from myApp

urlpatterns = [
    path("custom-admin/", include("myApp.admin_urls", namespace="custom_admin")),  # Custom admin dashboard
    path("", include("myApp.urls")),  # Main app URLs
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
