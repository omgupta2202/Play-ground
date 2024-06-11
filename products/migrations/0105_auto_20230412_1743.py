# Generated by Django 3.2.4 on 2023-04-12 15:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0104_auto_20230412_1739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'Series', 'verbose_name_plural': 'Series'},
        ),
        migrations.AddField(
            model_name='series',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 12, 15, 43, 21, 366520, tzinfo=utc)),
        ),
    ]
