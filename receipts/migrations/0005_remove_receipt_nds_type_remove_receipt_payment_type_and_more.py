# Generated by Django 4.0.6 on 2022-08-07 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0004_receipt_nds_type_receipt_operation_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='nds_type',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='payment_type',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='product_type',
        ),
    ]
