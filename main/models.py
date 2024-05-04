from django.db import models
from django.db.models import TextChoices


class Contact(models.Model):
    """Модель контактов
    - email: Электронная почта
    - country: Страна
    - city: Город
    - street: Улица
    - house_number: Номер дома
    - company: Связанная модель компании (Company)
    """
    email = models.EmailField(max_length=100, verbose_name="email")
    country = models.CharField(max_length=50, verbose_name="country")
    city = models.CharField(max_length=50, verbose_name="city")
    street = models.CharField(max_length=100, verbose_name="street")
    house_number = models.CharField(max_length=50, verbose_name="house_number")
    company = models.ForeignKey("Company",
                                related_name="company_contacts",
                                verbose_name="company_contact",
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email} - {self.country}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class CompanyStatus(TextChoices):
    """Модель для статуса компании
    - FACTORY: Завод
    - RETAIL_NETWORK: Розничная Сеть
    - INDIVIDUAL_ENTREPRENEUR: Индивидуальный Предприниматель
    """
    FACTORY = "FACTORY", "Завод"
    RETAIL_NETWORK = "RETAIL_NETWORK", "Розничная Сеть"
    INDIVIDUAL_ENTREPRENEUR = "INDIVIDUAL_ENTREPRENEUR", "Индивидуальный Предприниматель"


class Company(models.Model):
    """Модель Компании
    - status: Завод / Розничная Сеть / Индивидуальный Предприниматель
    - name: Наименование компании
    - provider: Поставщик. Не заполняется для статуса - Завод
    - debt: Задолженность перед поставщиком (provider)
    - date_created: Дата создания. Заполняется автоматически
    """
    status = models.CharField(max_length=30, verbose_name="company_status", choices=CompanyStatus.choices)
    name = models.CharField(max_length=255, verbose_name="company_name")
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="provider", blank=True, null=True)
    debt = models.FloatField(default=0, verbose_name="debt")
    date_created = models.DateField(auto_now_add=True, verbose_name="date_created")

    def __str__(self):
        return f'{self.name} | {self.status}'

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ["-date_created"]
