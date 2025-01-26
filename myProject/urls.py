from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from myApp import views

urlpatterns = [
    # Redirect /admin to custom admin
    path('admin/', views.redirect_to_custom_admin, name='redirect_to_custom_admin'),
    # Include custom admin URLs
    path('custom-admin/', include('myApp.admin_urls', namespace='custom_admin')),
    # Main app URLs
    path('', include('myApp.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
