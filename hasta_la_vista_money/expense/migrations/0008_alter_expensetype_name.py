# Generated by Django 4.2.6 on 2023-10-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            'expense',
            '0007_alter_expense_account_alter_expense_category_and_more',
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetype',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
