# Generated by Django 2.1.5 on 2021-09-03 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0017_auto_20210902_1802'),
        ('liniProduksi', '0048_auto_20210903_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetMingguan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('capaian', models.IntegerField(default=0)),
                ('minggu', models.DateField(null=True)),
                ('liniProduksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='liniProduksi.LiniProduksi', to_field='idLiniProduksi')),
                ('varian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Varian', to_field='idVarian')),
            ],
        ),
    ]