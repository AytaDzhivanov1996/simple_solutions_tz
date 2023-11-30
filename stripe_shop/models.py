from django.db import models


class Item(models.Model):
    
    name = models.CharField(max_length=128, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
