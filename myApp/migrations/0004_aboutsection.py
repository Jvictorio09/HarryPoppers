# Generated by Django 5.1.4 on 2024-12-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0003_service_alt_text_service_link_alter_service_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "heading",
                    models.CharField(
                        help_text="Heading for the about section", max_length=200
                    ),
                ),
                (
                    "subheading",
                    models.CharField(help_text="Subheading text", max_length=200),
                ),
                (
                    "description1",
                    models.TextField(help_text="First description paragraph"),
                ),
                (
                    "description2",
                    models.TextField(help_text="Second description paragraph"),
                ),
                (
                    "description3",
                    models.TextField(help_text="Third description paragraph"),
                ),
                (
                    "image1",
                    models.ImageField(
                        help_text="First image", upload_to="about_images/"
                    ),
                ),
                (
                    "image2",
                    models.ImageField(
                        help_text="Second image", upload_to="about_images/"
                    ),
                ),
                (
                    "image3",
                    models.ImageField(
                        help_text="Third image", upload_to="about_images/"
                    ),
                ),
            ],
        ),
    ]
