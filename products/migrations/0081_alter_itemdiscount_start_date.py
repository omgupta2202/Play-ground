# Generated by Django 3.2.4 on 2023-03-24 14:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0080_alter_itemdiscount_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 14, 41, 43, 982868, tzinfo=utc)),
        ),
    ]