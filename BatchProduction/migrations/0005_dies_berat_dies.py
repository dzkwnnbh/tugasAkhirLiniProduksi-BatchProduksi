# Generated by Django 2.1.5 on 2021-11-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatchProduction', '0004_proses_durasiproduksi'),
    ]

    operations = [
        migrations.AddField(
            model_name='dies',
            name='berat_dies',
            field=models.IntegerField(default=250),
            preserve_default=False,
        ),
    ]
