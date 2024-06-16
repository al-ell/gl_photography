# Generated by Django 3.2.25 on 2024-06-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prints',
            name='limited_edition',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='prints',
            name='friendly_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]