# Generated by Django 2.1.5 on 2021-08-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liniProduksi', '0025_auto_20210820_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liniproduksi',
            name='waktuMulaiIstirahat',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='liniproduksi',
            name='waktuSelesaiIstirahat',
            field=models.TimeField(),
        ),
    ]
