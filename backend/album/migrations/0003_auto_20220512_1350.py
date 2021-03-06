# Generated by Django 3.1 on 2022-05-12 10:50

import album.models.photo_page
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_photopage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photopage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[album.models.photo_page.validate_file_size], verbose_name='Загружаемое фото'),
        ),
    ]
