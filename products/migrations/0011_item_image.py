# Generated by Django 3.2 on 2023-02-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_genres_item_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
    ]
