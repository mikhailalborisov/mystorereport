from django.db import models


# Магазины торговой сети
class Store_as_st(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите наименнование магазина",
        verbose_name="Название магазина",
    )
    address = models.CharField(
        max_length=200,
        help_text="Введите адрес магазина",
        verbose_name="Адрес магазина",
    )


class Item(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите наименнование товара",
        verbose_name="Название товара",
    )
    price = models.FloatField(
        help_text="Введите цену товара",
        verbose_name="Цена товараа",
    )


class Sales_receipt(models.Model):
    total_sum = models.FloatField(
        help_text="Введите общую сумму чека",
        verbose_name="Общая сумма чека",
    )
    sale_time = models.DateField(
        null=True,
        blank=True,
        help_text="Введите время формирования чека",
        verbose_name="Время создания чека",
    )


class Sales(models.Model):
    item_id = models.ForeignKey(
        "Item",
        on_delete=models.CASCADE,
        help_text=" Выберите товар",
        verbose_name="Товар",
        null=True,
    )
    store_id = models.ForeignKey(
        "Store_as_st",
        on_delete=models.CASCADE,
        help_text=" Выберите магазин",
        verbose_name="Магазин",
        null=True,
    )
    sales_receipt_i = models.ForeignKey(
        "Sales_receipt",
        on_delete=models.CASCADE,
        help_text=" Выберите чек",
        verbose_name="Чек",
        null=True,
    )
