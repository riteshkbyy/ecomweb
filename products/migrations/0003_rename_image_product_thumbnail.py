# Generated by Django 5.0.6 on 2024-06-30 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slug_product_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='thumbnail',
        ),
    ]
