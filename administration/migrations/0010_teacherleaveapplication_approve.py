# Generated by Django 3.0 on 2020-09-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherleaveapplication',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
