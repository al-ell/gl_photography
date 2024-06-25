# Generated by Django 3.2.25 on 2024-06-25 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20240625_1053'),
        ('shop', '0004_prints_has_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='projects.project'),
        ),
        migrations.AlterField(
            model_name='prints',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='prints',
            name='image_url',
            field=models.URLField(default='', max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='prints',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='projects.photo'),
        ),
    ]
