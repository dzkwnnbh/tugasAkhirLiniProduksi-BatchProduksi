# Generated by Django 2.1.5 on 2021-08-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0008_auto_20210808_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='is_ganti',
            field=models.BooleanField(default=None),
        ),
    ]
