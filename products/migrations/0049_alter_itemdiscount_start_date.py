# Generated by Django 3.2.4 on 2023-03-10 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0048_alter_itemdiscount_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 13, 48, 38, 999954, tzinfo=utc)),
        ),
    ]
