from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=60)
    price = models.IntegerField(verbose_name="Цена")
    photo_path = models.ImageField(verbose_name="Фото товара", upload_to="photo/%Y/%m/%d/")

    def __str__(self):
        return self.name