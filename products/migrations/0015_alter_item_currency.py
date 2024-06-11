# Generated by Django 3.2 on 2023-02-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20230217_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('$', 'Usd'), ('€', 'Euro')], default='$', max_length=20),
        ),
    ]