from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

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
    image = CloudinaryField('image', help_text="Hero section image")
    button_text = models.CharField(max_length=50, help_text="Button text", default="Shop Now")
    button_url = models.URLField(help_text="Button link", default="#")

    def __str__(self):
        return self.title


from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import cloudinary.uploader

from io import BytesIO
from django.core.files.base import ContentFile
import cloudinary.uploader
import requests
from PIL import Image

@receiver(post_save, sender=HeroSection)
def resize_image(sender, instance, **kwargs):
    """
    Resize the uploaded image for Cloudinary storage.
    """
    if instance.image and instance.image.url:
        try:
            # ✅ Download the image from Cloudinary URL
            response = requests.get(instance.image.url, stream=True)
            response.raise_for_status()

            # ✅ Open the image from bytes
            img = Image.open(BytesIO(response.content))

            # ✅ Resize image
            img = img.resize((627, 717), Image.Resampling.LANCZOS)

            # ✅ Convert image to bytes for re-upload
            img_io = BytesIO()
            img.save(img_io, format="JPEG", quality=85)
            img_io.seek(0)

            # ✅ Upload resized image to Cloudinary
            upload_result = cloudinary.uploader.upload(img_io, folder="hero_images")

            # ✅ Update model with new image URL
            instance.image = upload_result["secure_url"]
            instance.save(update_fields=["image"])

        except Exception as e:
            print(f"Image resizing failed: {e}")


from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Category name (e.g., 'Strong Poppers', 'Beginner Friendly')")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the service (e.g., '10ml Poppers')")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the service (e.g., 950.00)")
    image = CloudinaryField('image', help_text="Image of the service")
    alt_text = models.CharField(max_length=150, help_text="Alt text for the image", default="Service image")
    link = models.URLField(default="#", help_text="URL for the service")
    description = models.TextField(blank=True, null=True, help_text="Description of the service")
    slug = models.SlugField(unique=True, blank=True, null=True)

    STRENGTH_LEVELS = [(25, "25%"), (50, "50%"), (75, "75%"), (100, "100%")]
    strength = models.IntegerField(choices=STRENGTH_LEVELS, default=50, help_text="Strength level of the product")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, help_text="Select a category for the product")  # ❌ No default for now!

    is_active = models.BooleanField(default=True, help_text="Uncheck to hide the product from listings.")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



from django.db import models

class AboutSection(models.Model):
    heading = models.CharField(max_length=200, help_text="Heading for the about section")
    subheading = models.CharField(max_length=200, help_text="Subheading text")
    description1 = models.TextField(help_text="First description paragraph")
    description2 = models.TextField(help_text="Second description paragraph")
    description3 = models.TextField(help_text="Third description paragraph")
    image1 = CloudinaryField('image', help_text="First image")  # ✅ Cloudinary Storage
    image2 = CloudinaryField('image', help_text="Second image")  # ✅ Cloudinary Storage
    image3 = CloudinaryField('image', help_text="Third image")  # ✅ Cloudinary Storage

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
    image = CloudinaryField('image', help_text="Image for the benefits section")  # ✅ Cloudinary Storage

    def __str__(self):
        return self.heading


from django.db import models

class ContactImage(models.Model):
    image = CloudinaryField('image', help_text="Image for the Contact section")  # ✅ Cloudinary Storage
    alt_text = models.CharField(max_length=150, help_text="Alt text for the image")

    def __str__(self):
        return self.alt_text or "Contact Image"


from django.db import models

class ContactImage(models.Model):
    image = CloudinaryField('image', help_text="Image for the Contact section")  # ✅ Cloudinary Storage
    alt_text = models.CharField(max_length=150, help_text="Alt text for the image")

    def __str__(self):
        return self.alt_text or "Contact Image"



class FAQ(models.Model):
    question = models.CharField(max_length=255, help_text="FAQ question")
    answer = models.TextField(help_text="FAQ answer")
    order = models.PositiveIntegerField(default=0, help_text="Order of the FAQ")
    image = CloudinaryField('image', blank=True, null=True, help_text="Optional image for the FAQ")  # ✅ Cloudinary Storage

    class Meta:
        ordering = ['order']  # FAQs will be ordered by their 'order' field

    def __str__(self):
        return self.question
    

class FAQSection(models.Model):
    title = models.CharField(max_length=255, help_text="Main title for the FAQ section")
    description = models.TextField(help_text="Short description for the FAQ section")
    side_image = CloudinaryField('image', blank=True, null=True, help_text="Image to display in the FAQ section")  # ✅ Cloudinary Storage

    def __str__(self):
        return self.title
