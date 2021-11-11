# Generated by Django 2.1.5 on 2021-11-01 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BatchProduction', '0001_initial'),
        ('produk', '0017_auto_20210902_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='dies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dies', to='BatchProduction.Dies', to_field='id_dies'),
        ),
        migrations.AddField(
            model_name='material',
            name='durasiProduksi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]