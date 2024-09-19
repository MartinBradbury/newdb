# Generated by Django 5.1.1 on 2024-09-19 22:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpjdwg51y/image/upload/v1726782033/k2wgf56y8stabvctolmu.png', max_length=255, verbose_name='image'),
        ),
    ]
