# Generated by Django 4.2.6 on 2023-10-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('income', '0008_alter_income_account_alter_income_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incometype',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
