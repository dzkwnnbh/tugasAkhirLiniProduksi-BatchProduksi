# Generated by Django 2.1.5 on 2021-08-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liniProduksi', '0010_auto_20210811_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='gangguan',
            name='kategori',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
