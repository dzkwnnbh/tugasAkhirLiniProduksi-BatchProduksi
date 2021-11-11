# Generated by Django 2.1.5 on 2021-11-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JadwalBatchProduction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetTahunan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField()),
                ('material', models.CharField(choices=[('V01', 'V01')], max_length=255)),
                ('target', models.IntegerField()),
                ('selesai', models.IntegerField(default=0)),
            ],
        ),
    ]