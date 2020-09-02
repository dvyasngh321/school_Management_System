# Generated by Django 3.0 on 2020-08-31 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('administration', '0006_merge_20200831_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default='1990-8-12'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Grade'),
        ),
    ]
