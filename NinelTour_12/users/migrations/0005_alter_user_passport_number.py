# Generated by Django 3.2.8 on 2021-11-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211111_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.CharField(max_length=6, unique=True, verbose_name='Номер паспорта'),
        ),
    ]
