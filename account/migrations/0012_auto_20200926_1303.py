# Generated by Django 3.0 on 2020-09-26 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200925_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacheraccount',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacheraccount',
            name='Staff_Username',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
