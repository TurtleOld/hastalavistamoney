# Generated by Django 4.2.2 on 2023-06-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_telegramuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='selected_account',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]