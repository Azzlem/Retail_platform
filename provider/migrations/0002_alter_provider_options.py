# Generated by Django 5.0.1 on 2024-01-23 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ('city',), 'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
    ]
