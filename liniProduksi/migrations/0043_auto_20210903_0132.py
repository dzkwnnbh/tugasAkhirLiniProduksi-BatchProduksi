# Generated by Django 2.1.5 on 2021-09-02 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0017_auto_20210902_1802'),
        ('liniProduksi', '0042_auto_20210902_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetHarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('tanggal', models.DateField()),
                ('waktuMulaiProduksi', models.TimeField()),
                ('waktuSelesaiProduksi', models.TimeField()),
                ('liniProduksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='liniProduksi.LiniProduksi', to_field='idLiniProduksi')),
                ('varian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Varian', to_field='idVarian')),
            ],
        ),
        migrations.RemoveField(
            model_name='produksiharian',
            name='persentaseCapaian',
        ),
        migrations.RemoveField(
            model_name='produksiharian',
            name='target',
        ),
    ]
