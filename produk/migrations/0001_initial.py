# Generated by Django 2.1.5 on 2021-08-01 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBrand', models.CharField(max_length=255)),
                ('namaBrand', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idMaterial', models.CharField(max_length=255)),
                ('namaMaterial', models.CharField(max_length=255)),
                ('namaSupplier', models.CharField(blank=True, max_length=255, null=True)),
                ('is_diubah', models.BooleanField(choices=[(0, 'Tidak'), (1, 'Iya')], default=False)),
                ('tanggalMaterialDiubah', models.DateField(blank=True, null=True)),
                ('keterangan', models.CharField(max_length=255, null=True)),
                ('penyusunProduk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produk.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('brand_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='produk.Brand')),
                ('idModel', models.CharField(max_length=255)),
                ('namaModel', models.CharField(max_length=255)),
            ],
            bases=('produk.brand',),
        ),
        migrations.CreateModel(
            name='Varian',
            fields=[
                ('model_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='produk.Model')),
                ('idVarian', models.CharField(max_length=255, unique=True)),
                ('namaVarian', models.CharField(max_length=255)),
                ('namaAtribut', models.CharField(max_length=255)),
                ('nilaiAtribut', models.CharField(max_length=255)),
            ],
            bases=('produk.model',),
        ),
        migrations.AddField(
            model_name='material',
            name='varian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Varian', to_field='idVarian'),
        ),
    ]
