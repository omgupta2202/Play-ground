# Generated by Django 3.2 on 2023-02-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230213_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='products.Item'),
        ),
    ]