# Generated by Django 3.2.4 on 2023-03-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_studios', '0002_remove_publisher_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255), editable=False, max_length=255),
        ),
    ]