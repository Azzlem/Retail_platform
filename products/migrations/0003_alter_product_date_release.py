# Generated by Django 5.0.1 on 2024-01-23 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options_product_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_release',
            field=models.DateField(default=datetime.datetime(2024, 1, 23, 19, 23, 26, 766433), verbose_name='Date Released'),
        ),
    ]