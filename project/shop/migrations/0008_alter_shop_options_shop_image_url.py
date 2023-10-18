# Generated by Django 4.2.5 on 2023-09-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_shop_update_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['-update_time'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='shop',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]