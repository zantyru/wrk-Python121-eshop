from django.db import models


class ItemType(models.Model):
    name = models.CharField(default="Неизвестный тип", max_length=40, unique=True)
    feature_types = models.ManyToManyField(
        'FeatureType',
        related_name='item_types', related_query_name='item_type'
    )

    def __str__(self):
        return f"{self.name}".capitalize()


class FeatureType(models.Model):

    class DataType(models.IntegerChoices):
        INTEGER = (1, "Целое число", )
        REAL = (2, "Вещественное число", )
        TEXT = (3, "Текст", )
        BOOLEAN = (4, "Да/нет", )
        DATETIME = (5, "Дата и время", )
        DATE = (6, "Дата", )
        TIME = (7, "Время", )

    name = models.CharField(unique=True, max_length=40)
    data_type = models.PositiveSmallIntegerField(
        choices=DataType.choices, default=DataType.TEXT
    )

    def __str__(self):
        return f"{self.name} ({self.data_type})"


class ItemFeature(models.Model):
    item = models.ForeignKey(
     'Item', on_delete=models.CASCADE,
     related_name='features', related_query_name='feature'
    )
    feature_type = models.ForeignKey(
     'FeatureType', on_delete=models.CASCADE,
     related_name='items', related_query_name='item'
    )
    value = models.CharField(default='', max_length=64)

    def __str__(self):
        return f"{self.item.name} ({self.feature_type.name}: {self.value})"


class Item(models.Model):
    name = models.CharField(default="", max_length=200)
    price = models.DecimalField(default=0, max_digits=13, decimal_places=2)
    item_type = models.ForeignKey(
        'ItemType', default=None, on_delete=models.CASCADE,
        related_name='items', related_query_name='item'
    )

    def __str__(self):
        return self.name


class ItemFeedback(models.Model):
    message = models.CharField(default="", max_length=5000)
    ranking = models.PositiveSmallIntegerField(default=0)
    item = models.ForeignKey(
        'Item', default=None, on_delete=models.CASCADE,
        related_name='feedbacks', related_query_name='feedback'
    )

    def __str__(self):
        return self.message[:30]
