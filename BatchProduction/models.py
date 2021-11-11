from django.db import models


class StasiunKerja(models.Model):
    # data stasiun kerja
    id_stasiun_kerja = models.CharField(max_length=255, unique=True)
    # nama_stasiun_kerja = models.CharField(max_length=255)
    # data produksi
    mulai_kerja = models.TimeField()
    selesai_kerja = models.TimeField()

    def save(self, *args, **kwargs):
        super(StasiunKerja, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id_stasiun_kerja)


class OperatorSK(models.Model):
    username = models.CharField(max_length=16, unique=True)
    nama = models.CharField(max_length=255)
    lokasi = models.ForeignKey(StasiunKerja, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(OperatorSK, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.username)


class Mesin(StasiunKerja):
    # data mesin
    id_mesin = models.CharField(max_length=5, unique=True)
    nama_mesin = models.CharField(max_length=255)
    # status_mesin = models.BooleanField(default=True, choices=[(1, 'Avaliable'), (0, 'Unavailable')])

    def save(self, *args, **kwargs):
        super(Mesin, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.nama_mesin)


class Proses(models.Model):
    # data proses
    id_proses = models.CharField(max_length=255, unique=True)
    nama_proses = models.CharField(max_length=255)
    mesin = models.ForeignKey('Mesin', on_delete=models.CASCADE, to_field='id_mesin')
    durasiProduksi = models.IntegerField()

    def save(self, *args, **kwargs):
        super(Proses, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.nama_proses)


class Dies(models.Model):
    # data dies
    id_dies = models.CharField(max_length=255, unique=True)
    # nama_dies = models.CharField(max_length=255)
    proses = models.ForeignKey('Proses', on_delete=models.CASCADE, to_field='id_proses')
    # data produksi
    durasi_setup = models.IntegerField()
    berat_dies = models.IntegerField()

    def save(self, *args, **kwargs):
        super(Dies, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id_dies)


# class Istirahat(models.Model):
#     mesin = models.ForeignKey(Mesin, on_delete=models.CASCADE, to_field='id_mesin')
#     # tanggal = models.DateField()
#     waktu_awal = models.TimeField(null=True, blank=True)
#     waktu_akhir = models.TimeField(null=True, blank=True)


# class Perawatan(models.Model):
#     mesin = models.ForeignKey(Mesin, on_delete=models.CASCADE, to_field='id_mesin')
#     is_usable = models.BooleanField(choices=[(1, 'Iya'), (0, 'Tidak')])
#     keterangan_perawatan = models.TextField()
#     tanggal_perawatan = models.DateField()
#     waktu_awal = models.TimeField()
#     waktu_akhir = models.TimeField()
