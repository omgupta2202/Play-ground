# Generated by Django 3.2.4 on 2023-03-23 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0077_alter_itemdiscount_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
            ],
        ),
        migrations.RemoveField(
            model_name='regionofactivation',
            name='name',
        ),
        migrations.AlterField(
            model_name='itemdiscount',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 15, 6, 13, 861261, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='regionofactivation',
            name='region',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.region'),
        ),
    ]