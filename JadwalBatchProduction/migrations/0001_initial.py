# Generated by Django 2.1.5 on 2021-11-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tp', models.CharField(max_length=255)),
                ('is_go', models.BooleanField(choices=[(1, 'Go'), (0, 'No Go')], default=True)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('mesin', models.CharField(blank=True, max_length=255, null=True)),
                ('stasiun_kerja', models.CharField(blank=True, max_length=255, null=True)),
                ('proses', models.CharField(blank=True, max_length=255, null=True)),
                ('dies', models.CharField(blank=True, max_length=255, null=True)),
                ('tanggal_mulai', models.DateTimeField(blank=True, null=True)),
                ('tanggal_selesai', models.DateTimeField(blank=True, null=True)),
                ('tanggal_selesai_asli', models.DateTimeField(null=True)),
                ('tanggal_mulai_asli', models.DateTimeField(null=True)),
            ],
        ),
    ]