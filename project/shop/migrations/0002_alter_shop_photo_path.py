# Generated by Django 4.2.5 on 2023-09-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='photo_path',
            field=models.ImageField(default='', upload_to='photo/%Y/%m/%d/', verbose_name='Фото товара'),
        ),
    ]
