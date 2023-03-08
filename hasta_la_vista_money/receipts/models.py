from django.db import models
from django.utils.translation import gettext_lazy as _

OPERATION_TYPES = (
    (1, _('Приход')),
    (2, _('Возврат прихода')),
    (3, _('Расход')),
    (4, _('Возврат расхода')),
)


class Customer(models.Model):
    name_seller = models.CharField(max_length=100)
    retail_place_address = models.CharField(null=True, max_length=100)
    retail_place = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name_seller


class Receipt(models.Model):
    receipt_date = models.DateTimeField()
    operation_type = models.IntegerField(
        null=True, blank=True, choices=OPERATION_TYPES,
    )
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='customer',
        related_name='customer',
    )
    product = models.ManyToManyField('Product', related_name='product')

    def __str__(self):
        return self.receipt_date


class Product(models.Model):
    product_name = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    nds_type = models.IntegerField(null=True, blank=True)
    nds_sum = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
