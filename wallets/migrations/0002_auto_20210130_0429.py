# Generated by Django 3.1.5 on 2021-01-30 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
