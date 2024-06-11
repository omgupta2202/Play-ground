# Generated by Django 3.2.4 on 2023-03-23 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0078_auto_20230323_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 15, 6, 28, 197338, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='regionofactivation',
            name='region',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='products.region'),
        ),
    ]
