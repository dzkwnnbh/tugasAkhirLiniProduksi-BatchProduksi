# Generated by Django 2.1.5 on 2021-08-03 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engineeringOrder', '0002_auto_20210803_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineeringorder',
            name='departemenPengusul',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='engineeringorder',
            name='keterangan',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='engineeringorder',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Material', unique=True),
        ),
        migrations.AlterField(
            model_name='engineeringorder',
            name='namaPengusul',
            field=models.CharField(max_length=255),
        ),
    ]
