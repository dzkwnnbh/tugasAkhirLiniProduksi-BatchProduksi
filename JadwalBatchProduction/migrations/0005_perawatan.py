# Generated by Django 2.1.5 on 2021-11-03 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BatchProduction', '0003_auto_20211103_1018'),
        ('JadwalBatchProduction', '0004_auto_20211103_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perawatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(choices=[(1, 'Iya'), (0, 'Tidak')])),
                ('keterangan_perawatan', models.TextField()),
                ('tanggal_perawatan', models.DateField()),
                ('waktu_awal', models.TimeField()),
                ('waktu_akhir', models.TimeField()),
                ('mesin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BatchProduction.Mesin', to_field='id_mesin')),
            ],
        ),
    ]
