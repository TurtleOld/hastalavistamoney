# Generated by Django 4.2.5 on 2023-09-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0008_remove_account_account_acc_name_ac_e74e62_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='account',
            index=models.Index(
                fields=['name_account'], name='account_acc_name_ac_e74e62_idx'
            ),
        ),
    ]
