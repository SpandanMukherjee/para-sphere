# Generated by Django 5.1.6 on 2025-02-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background_color',
            field=models.CharField(blank=True, default='#121212', max_length=7, null=True),
        ),
    ]
