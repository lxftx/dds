from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(verbose_name="Статус", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class OperationType(models.Model):
    name = models.CharField(verbose_name="Тип", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=100)
    operation_type = models.ForeignKey(OperationType, verbose_name="Тип", on_delete=models.CASCADE, related_name='categories')

    class Meta:
        unique_together = ('name', 'operation_type')
        ordering = ['name']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.operation_type.name} → {self.name}"

class SubCategory(models.Model):
    name = models.CharField(verbose_name="Подкатегория", max_length=100)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')
        ordering = ['name']
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return f"{self.category.name} → {self.name}"

class CashFlowRecord(models.Model):
    created_at = models.DateField(verbose_name="Время создания", default=timezone.now)
    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.PROTECT)
    operation_type = models.ForeignKey(OperationType, verbose_name="Тип", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, verbose_name="Подкатегория", on_delete=models.PROTECT)
    amount = models.DecimalField(verbose_name="Цена", help_text="Рублей", max_digits=12, decimal_places=2)
    comment = models.TextField(verbose_name="Комментарии", blank=True, null=True)

    def __str__(self):
        return f"{self.created_at} | {self.amount} ₽ | {self.status.name}"

    class Meta:
        ordering = ['created_at']
        verbose_name = "Средство"
        verbose_name_plural = "Средства"