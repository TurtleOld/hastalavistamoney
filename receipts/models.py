from django.db import models
from django.contrib.postgres.fields import ArrayField


class Receipt(models.Model):
    receipt_date = models.CharField(max_length=20)
    name_seller = models.CharField(max_length=150)
    product_information = ArrayField(ArrayField(
            models.CharField(max_length=1000), default=list
        )
    )
    total_sum = models.CharField(max_length=20)

