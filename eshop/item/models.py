from django.db import models


class ItemType(models.Model):
    name = models.CharField(default="Неизвестный тип", unique=True)


class ItemFeatureType(models.Model):

    class DataType(models.IntegerChoices):
        INTEGER = (1, "Целое число", )
        REAL = (2, "Вещественное число", )
        TEXT = (3, "Текст", )
        BOOLEAN = (4, "Да/нет", )
        DATETIME = (5, "Дата и время", )
        DATE = (6, "Дата", )
        TIME = (7, "Время", )

    name = models.CharField(unique=True)
    data_type = models.PositiveSmallIntegerField(choices=DataType.choices, default=DataType.TEXT)


class ItemFeature(models.Model):
    pass


class Item(models.Model):
    pass


class ItemFeedback(models.Model):
    pass
