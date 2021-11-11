from django.contrib import admin

from . import models

admin.site.register(models.StasiunKerja)
admin.site.register(models.Mesin)
admin.site.register(models.Proses)
admin.site.register(models.Dies)
# admin.site.register(models.Produksi)
# admin.site.register(models.HasilHeijunka)
# admin.site.register(models.JadwalBatchProduction)
