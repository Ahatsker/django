from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=60)
    price = models.IntegerField(verbose_name="Цена")
    photo_path = models.ImageField(verbose_name="Фото товара", upload_to="photo/%Y/%m/%d/", default='/photo/2023/09/08/pgadmin.png')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Категория"
        verbose_name_plural = "Категории"