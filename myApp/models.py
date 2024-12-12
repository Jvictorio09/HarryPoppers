from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    secondary_image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image  # For image resizing

class HeroSection(models.Model):
    title = models.CharField(max_length=200, help_text="Hero section title")
    subtitle = models.TextField(help_text="Hero section subtitle")
    description = models.TextField(help_text="Hero section description")
    image = models.ImageField(
        upload_to='',  # Images will be uploaded to the 'hero_images/' folder inside MEDIA_ROOT
        help_text="Hero section image"
    )
    button_text = models.CharField(max_length=50, help_text="Button text", default="Shop Now")
    button_url = models.URLField(help_text="Button link", default="#")

    def __str__(self):
        return self.title


# Signal to resize the image after the HeroSection object is saved
from PIL import Image

@receiver(post_save, sender=HeroSection)
def resize_image(sender, instance, **kwargs):
    """
    Resize the uploaded image to 627x717 pixels.
    """
    if instance.image:
        img_path = instance.image.path  # Get the file path of the uploaded image
        with Image.open(img_path) as img:
            # Resize the image to 627x717 while maintaining quality
            img = img.resize((627, 717), Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
            img.save(img_path)  # Save the resized image back to the same file

    
class Service(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the service (e.g., '10ml Poppers')")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the service (e.g., 950.00)")
    image = models.ImageField(upload_to='', help_text="Image of the service")
    alt_text = models.CharField(max_length=150, help_text="Alt text for the image", default="Service image")
    link = models.URLField(default="#", help_text="URL for the service")

    def __str__(self):
        return self.name


from django.db import models

class AboutSection(models.Model):
    heading = models.CharField(max_length=200, help_text="Heading for the about section")
    subheading = models.CharField(max_length=200, help_text="Subheading text")
    description1 = models.TextField(help_text="First description paragraph")
    description2 = models.TextField(help_text="Second description paragraph")
    description3 = models.TextField(help_text="Third description paragraph")
    image1 = models.ImageField(upload_to='about_images/', help_text="First image")
    image2 = models.ImageField(upload_to='about_images/', help_text="Second image")
    image3 = models.ImageField(upload_to='about_images/', help_text="Third image")

    def __str__(self):
        return self.heading


from django.db import models

class BenefitsSection(models.Model):
    heading = models.CharField(max_length=200, help_text="Main heading for the benefits section")
    subheading = models.CharField(max_length=200, help_text="Subheading for the section")
    description = models.TextField(help_text="Brief description of the benefits")
    benefit_1 = models.CharField(max_length=200, help_text="First benefit")
    benefit_2 = models.CharField(max_length=200, help_text="Second benefit")
    benefit_3 = models.CharField(max_length=200, help_text="Third benefit")
    benefit_4 = models.CharField(max_length=200, help_text="Fourth benefit")
    image = models.ImageField(upload_to='benefits_images/', help_text="Image for the benefits section")

    def __str__(self):
        return self.heading


from django.db import models

class ContactImage(models.Model):
    image = models.ImageField(upload_to='contact_images/', help_text="Image for the Contact section")
    alt_text = models.CharField(max_length=150, help_text="Alt text for the image")

    def __str__(self):
        return self.alt_text or "Contact Image"


from django.db import models

class ContactImage(models.Model):
    image = models.ImageField(upload_to='contact_images/', help_text="Image for the Contact section")
    alt_text = models.CharField(max_length=150, help_text="Alt text for the image")

    def __str__(self):
        return self.alt_text or "Contact Image"
