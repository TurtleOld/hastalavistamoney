# Generated by Django 4.2.2 on 2023-06-26 21:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensetype',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.account'),
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='expense.expensetype'),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
