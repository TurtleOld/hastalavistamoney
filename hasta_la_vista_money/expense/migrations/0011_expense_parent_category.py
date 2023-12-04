# Generated by Django 4.2.7 on 2023-11-12 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("expense", "0010_rename_expensetype_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="parent_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subcategories",
                to="expense.expense",
            ),
        ),
    ]