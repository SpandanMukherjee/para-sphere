# Generated by Django 5.1.6 on 2025-02-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_color',
            field=models.CharField(blank=True, default='121212', help_text='Enter a hex colour code, e.g., #ff5733', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='backgrounds/'),
        ),
    ]
