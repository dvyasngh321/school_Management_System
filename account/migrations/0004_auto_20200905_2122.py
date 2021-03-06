# Generated by Django 3.0 on 2020-09-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_prev_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='prev_balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
