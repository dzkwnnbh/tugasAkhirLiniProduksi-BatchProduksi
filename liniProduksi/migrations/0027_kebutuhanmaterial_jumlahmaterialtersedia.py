# Generated by Django 2.1.5 on 2021-08-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liniProduksi', '0026_auto_20210820_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='kebutuhanmaterial',
            name='jumlahMaterialTersedia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
