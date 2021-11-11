from django.contrib import admin
from . import models


class JadwalAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# class TargetProduksiAdmin(admin.ModelAdmin):
#     readonly_fields = [
#         'tanggal_mulai_asli', 'tanggal_selesai_asli'
#     ]


# admin.site.register(models.ProduksiHarian, TargetProduksiAdmin)
admin.site.register(models.Jadwal, JadwalAdmin)
