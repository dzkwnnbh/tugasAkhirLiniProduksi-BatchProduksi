# Generated by Django 2.1.5 on 2021-09-02 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liniProduksi', '0041_auto_20210902_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waktuistirahat',
            name='produksiHarian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liniProduksi.ProduksiHarian'),
        ),
    ]
