from django.urls import path
from . import views

app_name = "custom_admin"  # Required for the namespace to work

urlpatterns = [
    path("", views.admin_landing_page, name="admin_landing_page"),
    path("hero-section/", views.hero_section, name="hero_section"),
    path("about-section/", views.about_section, name="about_section"),
    path("products/", views.products, name="products"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("products/delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path("benefits-section/", views.benefits_section, name="benefits_section"),
    path("contact-images/", views.contact_images, name="contact_images"),
    path("contact-images/edit/<int:image_id>/", views.edit_contact_image, name="edit_contact_image"),
    path("contact-images/delete/<int:image_id>/", views.delete_contact_image, name="delete_contact_image"),
    path("faqs/", views.manage_faqs, name="manage_faqs"),

    path("login/", views.admin_login, name="login"),
    path("logout/", views.admin_logout, name="logout"),

    path("manage-access/", views.create_user_profile, name="manage_access"),
    path("ajax/change-password/", views.change_password, name="change_password"),
     
    path("categories/", views.manage_categories, name="manage_categories"),
    path("add-category/", views.add_category, name="add_category"),
    path("edit-category/<int:category_id>/", views.edit_category, name="edit_category"),
    path("delete-category/<int:category_id>/", views.delete_category, name="delete_category"),
    
    # ✅ AJAX Category Creation
    path("ajax/add-category/", views.add_category_ajax, name="add_category_ajax"),
    
    path("toggle-active/<int:product_id>/", views.toggle_product_active, name="toggle_product_active"),
    path("delete-product/<int:product_id>/", views.delete_product, name="delete_product"),

    path("mass-delete/", views.mass_delete_products, name="mass_delete_products"),
    


]
