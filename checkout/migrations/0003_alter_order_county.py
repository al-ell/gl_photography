# Generated by Django 3.2.25 on 2024-06-05 12:53

from django.db import migrations
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20240604_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=django_countries.fields.CountryField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
