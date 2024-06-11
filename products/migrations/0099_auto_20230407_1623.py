# Generated by Django 3.2.4 on 2023-04-07 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('reviews', '0001_initial'),
        ('products', '0098_auto_20230406_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='series_games',
            field=models.ManyToManyField(blank=True, null=True, related_name='_products_item_series_games_+', to='products.Item', verbose_name='Series game'),
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 7, 14, 23, 21, 67551, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Addon',
        ),
    ]