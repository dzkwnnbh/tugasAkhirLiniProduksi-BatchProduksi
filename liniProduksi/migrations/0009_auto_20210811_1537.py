# Generated by Django 2.1.5 on 2021-08-11 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liniProduksi', '0008_auto_20210811_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gangguan',
            old_name='penyebab',
            new_name='keterangan',
        ),
    ]