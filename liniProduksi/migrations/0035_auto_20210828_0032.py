# Generated by Django 2.1.5 on 2021-08-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liniProduksi', '0034_auto_20210828_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='namaLengkap',
            field=models.CharField(max_length=255),
        ),
    ]
