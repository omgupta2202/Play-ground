# Generated by Django 3.2.4 on 2023-03-10 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0044_auto_20230310_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 13, 8, 40, 829123, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemplatform',
            name='name',
            field=models.CharField(blank=True, choices=[('Steam', 'Steam'), ('Xbox', 'Xbox'), ('Rockstar Games', 'Rockstar Games'), ('Uplay', 'Uplay'), ('Epic Games', 'Epic Games')], max_length=100),
        ),
    ]