# Generated by Django 3.0 on 2020-09-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
