from django import forms
from django.contrib.auth.models import User
from . import models
from produk import models as models_produk


class MesinForm(forms.ModelForm):
    class Meta:
        model = models.Mesin
        fields = [
            'id_stasiun_kerja',
            # 'nama_stasiun_kerja',
            'id_mesin',
            'nama_mesin',
            'mulai_kerja',
            'selesai_kerja'
        ]
        labels = {
            'id_stasiun_kerja': 'ID Stasiun Kerja',
            'nama_stasiun_kerja': 'Nama Stasiun Kerja',
            'id_mesin': 'ID Mesin',
            'nama_mesin': 'Nama Mesin',
            'mulai_kerja': 'Jam Masuk',
            'selesai_kerja': 'Jam Pulang'
        }
        widgets = {
            'id_stasiun_kerja': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nama_stasiun_kerja': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'id_mesin': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nama_mesin': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'mulai_kerja': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
            'selesai_kerja': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            )
        }


class OperatorSKForm(forms.ModelForm):
    class Meta:
        model = models.OperatorSK
        fields = [
            'username',
            'nama',
            'lokasi'
        ]
        labels = {
            'username': 'Username',
            'nama': 'Nama Operator',
            'lokasi': 'Lokasi Kerja',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lokasi': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }


class ProsesForm(forms.ModelForm):
    class Meta:
        model = models.Proses
        fields = [
            'id_proses',
            'nama_proses',
            'mesin',
            'durasiProduksi'
        ]
        labels = {
            'id_proses': 'ID Proses',
            'nama_proses': 'Nama Proses',
            'mesin': 'Mesin',
            'durasiProduksi': 'Durasi Produksi',
        }
        widgets = {
            'id_proses': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nama_proses': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'mesin': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'durasiProduksi': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class DiesForm(forms.ModelForm):
    class Meta:
        model = models.Dies
        fields = [
            'id_dies',
            # 'nama_dies',
            'proses',
            'berat_dies',
            'durasi_setup',
        ]
        labels = {
            'id_dies': 'ID Dies',
            # 'nama_dies': 'Nama Dies',
            'berat_dies': 'Berat Dies',
            'proses': 'Proses',
            'durasi_setup': 'Durasi Setup (menit)'
        }
        widgets = {
            'id_dies': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nama_dies': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'proses': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'durasi_setup': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


# class PerawatanForm(forms.ModelForm):
#     class Meta:
#         model = models.Perawatan
#         fields = [
#             'mesin',
#             'is_usable',
#             'keterangan_perawatan',
#             'tanggal_perawatan',
#             'waktu_awal',
#             'waktu_akhir'
#         ]
#         labels = {
#             'mesin': 'Mesin',
#             'keterangan_perawatan': 'Keterangan',
#             'is_usable': 'Apakah mesin masih bisa digunakan?',
#             'tanggal_perawatan': 'Tanggal',
#             'waktu_awal': 'Waktu Awal',
#             'waktu_akhir': 'Waktu Akhir'
#
#         }
#         widgets = {
#             'mesin': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#             'keterangan_perawatan': forms.Textarea(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'is_usable': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#             'tanggal_perawatan': forms.DateInput(
#                 attrs={
#                     'type': 'date',
#                     'class': 'form-control'
#                 }
#             ),
#             'waktu_awal': forms.TimeInput(
#                 attrs={
#                     'type': 'time',
#                     'class': 'form-control'
#                 }
#             ),
#             'waktu_akhir': forms.TimeInput(
#                 attrs={
#                     'type': 'time',
#                     'class': 'form-control'
#                 }
#             ),
#         }


# class IstirahatForm(forms.ModelForm):
#     class Meta:
#         model = models.Istirahat
#         fields = [
#             'mesin',
#             # 'tanggal',
#             'waktu_awal',
#             'waktu_akhir'
#         ]
#         labels = {
#             'mesin': 'Mesin',
#             'tanggal': 'Tanggal',
#             'waktu_awal': 'Jam Istirahat',
#             'waktu_akhir': ''
#         }
#         widgets = {
#             'mesin': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#             'tanggal': forms.DateInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'waktu_awal': forms.TimeInput(
#                 attrs={
#                     'type': 'time',
#                     'class': 'form-control'
#                 }
#             ),
#             'waktu_akhir': forms.TimeInput(
#                 attrs={
#                     'type': 'time',
#                     'class': 'form-control'
#                 }
#             ),
#         }