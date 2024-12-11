# Generated by Django 5.1.4 on 2024-12-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0002_alter_herosection_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="alt_text",
            field=models.CharField(
                default="Service image",
                help_text="Alt text for the image",
                max_length=150,
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="link",
            field=models.URLField(default="#", help_text="URL for the service"),
        ),
        migrations.AlterField(
            model_name="service",
            name="image",
            field=models.ImageField(help_text="Image of the service", upload_to=""),
        ),
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(
                help_text="Name of the service (e.g., '10ml Poppers')", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Price of the service (e.g., 950.00)",
                max_digits=10,
            ),
        ),
    ]