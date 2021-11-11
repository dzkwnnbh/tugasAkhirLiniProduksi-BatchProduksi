import datetime

import pytz
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from produk.models import Material, Varian
from BatchProduction.models import Mesin, Proses, Dies


class TargetTahunan(models.Model):
    CHOICESMAT = []
    for i in Varian.objects.all().values_list('idVarian', flat=True).distinct():
        CHOICESMAT.append((i, i))
    # for i in Material.objects.filter(durasiProduksi__isnull=False, is_berlaku=1).values_list('idMaterial', flat=True).distinct():
    #     CHOICESMAT.append((i, i))
    tahun = models.IntegerField()
    material = models.CharField(max_length=255, choices=CHOICESMAT)
    # material = models.ForeignKey(Varian, on_delete=models.CASCADE, to_field='idVarian')
    target = models.IntegerField()
    selesai = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(TargetTahunan, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.material)


class TargetBulanan(models.Model):
    CHOICESMAT = []
    # for i in Material.objects.filter(durasiProduksi__isnull=False, is_berlaku=1).values_list('idMaterial', flat=True).distinct():
    #     CHOICESMAT.append((i, i))
    for i in Varian.objects.all().values_list('idVarian', flat=True).distinct():
        CHOICESMAT.append((i, i))
    CHOICESTHN = []
    for i in TargetTahunan.objects.all().values_list('tahun', flat=True).distinct():
        CHOICESTHN.append((i, i))
    CHOICESBLN = [
        (1, 'Januari'),
        (2, 'Februari'),
        (3, 'Maret'),
        (4, 'April'),
        (5, 'Mei'),
        (6, 'Juni'),
        (7, 'Juli'),
        (8, 'Agustus'),
        (9, 'September'),
        (10, 'Oktober'),
        (11, 'November'),
        (12, 'Desember'),
    ]
    material = models.CharField(max_length=255, choices=CHOICESMAT)
    # material = models.ForeignKey(Varian, on_delete=models.CASCADE, to_field='idVarian')
    target = models.IntegerField()
    selesai = models.IntegerField(default=0)
    bulan = models.IntegerField(choices=CHOICESBLN)
    tahun = models.IntegerField(choices=CHOICESTHN)

    def save(self, *args, **kwargs):
        super(TargetBulanan, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.material)


class TargetMingguan(models.Model):
    CHOICESMAT = []
    # for i in Material.objects.filter(durasiProduksi__isnull=False, is_berlaku=1).values_list('idMaterial', flat=True).distinct():
    #     CHOICESMAT.append((i, i))
    for i in Varian.objects.all().values_list('idVarian', flat=True).distinct():
        CHOICESMAT.append((i, i))
    CHOICESTHN = []
    for i in TargetTahunan.objects.all().values_list('tahun', flat=True).distinct():
        CHOICESTHN.append((i, i))
    material = models.CharField(max_length=255, choices=CHOICESMAT)
    # material = models.ForeignKey(Varian, on_delete=models.CASCADE, to_field='idVarian')
    target = models.IntegerField()
    selesai = models.IntegerField(default=0)
    minggu = models.IntegerField()
    tahun = models.IntegerField(choices=CHOICESTHN)

    def save(self, *args, **kwargs):
        super(TargetMingguan, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.material)


class TargetHarian(models.Model):
    tanggal = models.DateField(unique=True)
    waktumulai = models.TimeField(null=True)
    waktuselesai = models.TextField(null=True)
    is_digabung = models.CharField(choices=[('Gabung', 'Gabung'), ('Tidak', 'Tidak')], max_length=6)
    is_libur = models.BooleanField(default=False)
    is_dijadwal = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(TargetHarian, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.tanggal)


class ProduksiHarian(models.Model):
    # data produksi
    # CHOICESTHN = []
    # for i in TargetTahunan.objects.all().values_list('tahun', flat=True).distinct():
    #     CHOICESTHN.append((i, i))
    CHOICESMAT = []
    # for i in Material.objects.filter(durasiProduksi__isnull=False, is_berlaku=1).values_list('idMaterial', flat=True).distinct():
    #     CHOICESMAT.append((i, i))
    for i in Varian.objects.all().values_list('idVarian', flat=True).distinct():
        CHOICESMAT.append((i, i))
    material = models.CharField(max_length=255, choices=CHOICESMAT)
    # material = models.ForeignKey(Varian, on_delete=models.CASCADE, to_field='idVarian')
    target = models.IntegerField()
    selesai = models.IntegerField(default=0)
    tanggal = models.DateField()

    # tahun = models.IntegerField(choices=CHOICESTHN)

    def save(self, *args, **kwargs):
        super(ProduksiHarian, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.material)
    # varian = models.ForeignKey(Varian, on_delete=models.CASCADE)
    # jumlah = models.IntegerField()
    # CHOICES = [('Dibuat', 'Dibuat'), ('Menunggu', 'Menunggu'), ('Mulai', 'Mulai'), ('Selesai', 'Selesai')]
    # status = models.CharField(choices=CHOICES, max_length=255, default='Dibuat')
    # minggu = models.IntegerField(unique=True)
    # tanggal_selesai = models.DateField(null=True)
    # tanggal_mulai_asli = models.DateField(null=True)
    # tanggal_selesai_asli = models.DateField(null=True)
    #
    # def save(self, *args, **kwargs):
    #     super(ProduksiHarian, self).save(*args, **kwargs)
    #
    # def __str__(self):
    #     return str(self.material) + ' ' + str(self.jumlah)


class Jadwal(models.Model):
    # data produksi
    id_tp = models.CharField(max_length=255)
    is_go = models.BooleanField(default=True, choices=[(1, 'Go'), (0, 'No Go')])
    # varian = models.CharField(max_length=255)
    material = models.CharField(max_length=255, null=True, blank=True)
    mesin = models.CharField(max_length=255, null=True, blank=True)
    stasiun_kerja = models.CharField(max_length=255, null=True, blank=True)
    proses = models.CharField(max_length=255, null=True, blank=True)
    dies = models.CharField(max_length=255, null=True, blank=True)
    # operator = models.CharField(max_length=255, blank=True)
    # data jadwal
    tanggal_mulai = models.DateTimeField(null=True, blank=True)
    tanggal_selesai = models.DateTimeField(null=True, blank=True)
    tanggal_selesai_asli = models.DateTimeField(null=True)
    tanggal_mulai_asli = models.DateTimeField(null=True)
    # grafik = models.ImageField(upload_to='JadwalBatchProduction/grafik/')

    def save(self, *args, **kwargs):
        super(Jadwal, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.proses) + ' ' + str(self.tanggal_mulai) + ' s/d ' + str(self.tanggal_selesai)


# class Operator(models.Model):
#     id_operator = models.CharField(max_length=255)
#     nama_operator = models.CharField(max_length=255)
#     stasiun_kerja = models.OneToOneField(StasiunKerja, on_delete=models.CASCADE, to_field='id_stasiun_kerja')
#
#     def save(self, *args, **kwargs):
#         super(Operator, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.nama_operator)


# class Istirahat(models.Model):
#     # id_prodsharian = models.ForeignKey('TargetHarian', on_delete=models.CASCADE)
#     # jenis_break = models.CharField(choices=[('Istirahat', 'Istirahat'), ('Libur', 'Libur')], max_length=9)
#     # tanggal = models.DateField(null=True, blank=True)
#     mesin = models.ForeignKey(Mesin, on_delete=models.CASCADE, to_field='id_mesin')
#     waktu_awal = models.TimeField(null=True, blank=True)
#     waktu_akhir = models.TimeField(null=True, blank=True)
#
#
# class Perawatan(models.Model):
#     # id_perawatan = models.CharField(max_length=255, unique=True)
#     mesin = models.ForeignKey(Mesin, on_delete=models.CASCADE, to_field='id_mesin')
#     # namaPengusul = models.CharField(max_length=255)
#     # departemenPengusul = models.CharField(max_length=255)
#     # keterangan_kerusakan = models.TextField()
#     is_usable = models.BooleanField(choices=[(1, 'Iya'), (0, 'Tidak')])
#     keterangan_perawatan = models.TextField()
#     # is_fixed = models.BooleanField(default=False, choices=[(1, 'Fixed'), (0, 'Not Fixed')])
#     tanggal_perawatan = models.DateField()
#     waktu_awal = models.TimeField()
#     waktu_akhir = models.TimeField()
#     # tanggal_diperbaiki = models.DateTimeField(null=True, blank=True)


class Istirahat(models.Model):
#     id_tp = models.ForeignKey('ProduksiHarian', on_delete=models.CASCADE)
#     jenis_istirahat = models.CharField(choices=[('Istirahat', 'Istirahat'), ('Libur', 'Libur')], max_length=9)
    tanggal = models.DateField(null=True, blank=True)
    waktu_awal = models.TimeField(null=True, blank=True)
    waktu_akhir = models.TimeField(null=True, blank=True)


class Perawatan(models.Model):
    mesin = models.ForeignKey(Mesin, on_delete=models.CASCADE, to_field='id_mesin')
    is_usable = models.BooleanField(choices=[(1, 'Iya'), (0, 'Tidak')])
    keterangan_perawatan = models.TextField()
    tanggal_perawatan = models.DateField()
    waktu_awal = models.TimeField()
    waktu_akhir = models.TimeField()
