# Generated by Django 4.2.11 on 2025-02-01 03:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0012_category_service_is_active_service_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutsection",
            name="image1",
            field=cloudinary.models.CloudinaryField(
                help_text="First image", max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="aboutsection",
            name="image2",
            field=cloudinary.models.CloudinaryField(
                help_text="Second image", max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="aboutsection",
            name="image3",
            field=cloudinary.models.CloudinaryField(
                help_text="Third image", max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="benefitssection",
            name="image",
            field=cloudinary.models.CloudinaryField(
                help_text="Image for the benefits section",
                max_length=255,
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="contactimage",
            name="image",
            field=cloudinary.models.CloudinaryField(
                help_text="Image for the Contact section",
                max_length=255,
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="faq",
            name="image",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                help_text="Optional image for the FAQ",
                max_length=255,
                null=True,
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="faqsection",
            name="side_image",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                help_text="Image to display in the FAQ section",
                max_length=255,
                null=True,
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="herosection",
            name="image",
            field=cloudinary.models.CloudinaryField(
                help_text="Hero section image", max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="image",
            field=cloudinary.models.CloudinaryField(
                help_text="Image of the service", max_length=255, verbose_name="image"
            ),
        ),
    ]
