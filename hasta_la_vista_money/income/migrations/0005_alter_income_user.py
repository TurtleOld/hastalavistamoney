# Generated by Django 4.2.5 on 2023-09-21 00:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('income', '0004_alter_income_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
