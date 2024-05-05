from django.db import models
from main.models import Company


class Product(models.Model):
    """Модель продукта
    - name: Наименование
    - model: Модель продукта
    - release_date: Дата выхода на рынок
    - company: Компания в которой находится продукт, связаная модель (Company)
    - quantity: Количество продукта
    - price: Цена"""

    name = models.CharField(max_length=255, verbose_name="product_name")
    model = models.CharField(max_length=255, verbose_name="product_model")
    release_date = models.DateField(verbose_name="product_release_date")
    company = models.ForeignKey(Company,
                                verbose_name="company_name",
                                related_name="company_products",
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
