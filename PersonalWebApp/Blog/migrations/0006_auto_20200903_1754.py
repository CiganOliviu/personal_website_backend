# Generated by Django 3.0.8 on 2020-09-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20200903_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='introduction',
            field=models.TextField(default='', unique=True),
        ),
    ]