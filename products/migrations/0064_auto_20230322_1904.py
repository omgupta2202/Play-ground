# Generated by Django 3.2.4 on 2023-03-22 18:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0063_auto_20230322_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tagline',
            field=models.CharField(default='Game is coming', max_length=150, verbose_name='Tagline'),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 18, 4, 22, 723454, tzinfo=utc)),
        ),
    ]