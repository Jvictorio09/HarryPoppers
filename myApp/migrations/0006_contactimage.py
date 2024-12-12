# Generated by Django 5.1.4 on 2024-12-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0005_benefitssection"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactImage",
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
                    "image",
                    models.ImageField(
                        help_text="Image for the Contact section",
                        upload_to="contact_images/",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        help_text="Alt text for the image", max_length=150
                    ),
                ),
            ],
        ),
    ]