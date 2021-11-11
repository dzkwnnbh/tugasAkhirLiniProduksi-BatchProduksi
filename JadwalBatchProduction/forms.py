from django import forms
from django.contrib.auth.models import User
from . import models
from produk import models as models_produk


class TargetTahunanForm(forms.ModelForm):
    class Meta:
        model = models.TargetTahunan
        fields = [
            'material',
            'tahun',
            'target',
        ]

        labels = {
            'material': 'ID Material',
            'tahun': 'Tahun',
            'target': 'Target Produksi',
        }

        widgets = {
            'material': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'tahun': forms.NumberInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'target': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class TargetBulananForm(forms.ModelForm):
    class Meta:
        model = models.TargetBulanan
        fields = [
            'material',
            'bulan',
            'tahun',
            'target',
        ]

        labels = {
            'material': 'ID Material',
            'bulan': 'Bulan ke-',
            'tahun': 'Tahun',
            'target': 'Target Produksi',
        }

        widgets = {
            'material': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'bulan': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'tahun': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'target': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class TargetMingguanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TargetMingguanForm, self).__init__(*args, **kwargs)
        self.fields['tahun'].label_from_instance = lambda obj: "%s" % (
            obj.tahun
        )

    class Meta:
        model = models.TargetMingguan
        fields = [
            'material',
            'minggu',
            'tahun',
            'target',
        ]

        labels = {
            'material': 'ID Material',
            'minggu': 'Minggu ke-',
            'tahun': 'Tahun',
            'target': 'Target Produksi',
        }

        widgets = {
            'material': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'minggu': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tahun': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'target': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class TargetHarianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TargetHarianForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.TargetHarian
        fields = [
            'tanggal',
            'is_digabung'
        ]
        labels = {
            'tanggal': 'Tanggal',
            'is_digabung': 'Jika ada komponen penyusun yang sama untuk produksi lebih dari satu varian, apakah komponen tersebut digabung?'
        }
        widgets = {
            'tanggal': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'is_digabung': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }


class ProduksiHarianForm(forms.ModelForm):
    class Meta:
        model = models.ProduksiHarian
        fields = [
            'material',
            'target',
        ]

        labels = {
            'material': 'ID Material',
            'target': 'Target Produksi',
        }

        widgets = {
            'material': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'target': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


# class BreakForm(forms.ModelForm):
#     class Meta:
#         model = models.Break
#         fields = [
#             'jenis_break',
#         ]
#         labels = {
#             'jenis_break': 'Jenis Break',
#         }
#         widgets = {
#             'jenis_break': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#         }


# class PerawatanForm(forms.ModelForm):
#     class Meta:
#         model = models.Perawatan
#         fields = [
#             # 'id_perawatan',
#             'mesin',
#             # 'namaPengusul',
#             # 'departemenPengusul',
#             'is_usable',
#             'keterangan_perawatan',
#             'tanggal_perawatan',
#             'waktu_awal',
#             'waktu_akhir'
#         ]
#         labels = {
#             # 'id_perawatan': 'ID Perawatan',
#             'mesin': 'Mesin',
#             # 'namaPengusul': 'Nama Pengusul',
#             # 'departemenPengusul': 'Departemen',
#             'keterangan_perawatan': 'Keterangan',
#             'is_usable': 'Apakah mesin masih bisa digunakan?',
#             'tanggal_perawatan': 'Tanggal',
#             'waktu_awal': 'Waktu Awal',
#             'waktu_akhir': 'Waktu Akhir'
#
#         }
#         widgets = {
#             # 'id_kerusakan': forms.TextInput(
#             #     attrs={
#             #         'class': 'form-control'
#             #     }
#             # ),
#             'mesin': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#             # 'namaPengusul': forms.TextInput(
#             #     attrs={
#             #         'class': 'form-control',
#             #     }
#             # ),
#             # 'departemenPengusul': forms.TextInput(
#             #     attrs={
#             #         'class': 'form-control',
#             #     }
#             # ),
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
#
#
# class IstirahatForm(forms.ModelForm):
#     class Meta:
#         model = models.Istirahat
#         fields = [
#             'mesin',
#             'waktu_awal',
#             'waktu_akhir'
#         ]
#         labels = {
#             'mesin': 'Mesin',
#             'waktu_awal': 'Jam Istirahat',
#             'waktu_akhir': ''
#         }
#         widgets = {
#             'mesin': forms.Select(
#                 attrs={
#                     'class': 'form-select'
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


# class LiburForm(forms.ModelForm):
#     class Meta:
#         model = models.Break
#         fields = [
#             'tanggal',
#         ]
#         labels = {
#             'tanggal': 'Tanggal Hari Libur',
#         }
#         widgets = {
#             'tanggal': forms.DateTimeInput(
#                 attrs={
#                     'type': 'date',
#                     'class': 'form-control'
#                 }
#             ),
#         }


# class TargetProduksiForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(TargetProduksiForm, self).__init__(*args, **kwargs)
#         # self.fields['varian'].queryset = models_produk.Material.objects.filter(penyusunProduk__isnull=True)
#         # self.fields['varian'].label_from_instance = lambda obj: "%s" % (
#         #     obj.varian
#         # )
#
#     class Meta:
#         model = models.ProduksiHarian
#         fields = [
#             'varian',
#             'jumlah',
#             'minggu',
#             # 'tanggal_selesai'
#         ]
#         labels = {
#             'varian': 'Varian',
#             'jumlah': 'Jumlah',
#             'minggu': 'Minggu ke-'
#         }
#         widgets = {
#             'varian': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#             'jumlah': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'minggu': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'tanggal_selesai': forms.DateInput(
#                 attrs={
#                     'type': 'date',
#                     'class': 'form-control'
#                 }
#             ),
#         }


# class OperatorForm(forms.ModelForm):
#     class Meta:
#         model = models.Operator
#         fields = [
#             'id_operator',
#             'nama_operator',
#             'stasiun_kerja'
#         ]
#         labels = {
#             'id_operator': 'ID Operator',
#             'nama_operator': 'Nama Operator',
#             'stasiun_kerja': 'Stasiun Kerja'
#         }
#         widgets = {
#             'id_operator': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'nama_operator': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'stasiun_kerja': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#         }


# class JadwalForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(JadwalForm, self).__init__(*args, **kwargs)
#         # self.fields['operator'].queryset = User.objects.all()
#         # self.fields['operator'].label_from_instance = lambda obj: "%s %s" % (obj.first_name, obj.last_name)
#         self.fields['material'].queryset = models.ProduksiHarian.objects.all()
#         self.fields['material'].label_from_instance = lambda obj: "%s (%s)" % (obj.material, obj.jumlah)
#         self.fields['proses'].queryset = models.Proses.objects.all()
#         self.fields['proses'].label_from_instance = lambda obj: "%s (%s)" % (obj.nama_proses, obj.mesin)
#
#     class Meta:
#         model = models.JadwalBatchProduction
#         fields = [
#             'material',
#             'proses',
#             # 'dies',
#             # 'operator',
#             'tanggal_mulai',
#             'tanggal_selesai',
#         ]
#         labels = {
#             'material': 'Material & Target',
#             'proses': 'Proses & Mesin',
#             # 'dies': 'Dies',
#             # 'operator': 'Operator',
#             'tanggal_mulai': 'Tanggal Mulai',
#             'tanggal_selesai': 'Tanggal Selesai'
#         }
#         widgets = {
#             'material': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#             'proses': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#             # 'dies': forms.Select(
#             #     attrs={
#             #         'class': 'form-select'
#             #     }
#             # ),
#             # 'operator': forms.Select(
#             #     attrs={
#             #         'class': 'form-select'
#             #     }
#             # ),
#             'tanggal_mulai': forms.DateInput(
#                 attrs={
#                     'type': 'date',
#                     'class': 'form-control'
#                 }
#             ),
#             'tanggal_selesai': forms.DateInput(
#                 attrs={
#                     'type': 'date',
#                     'class': 'form-control'
#                 }
#             )
#         }



# class PerbaikanForm(forms.ModelForm):
#     class Meta:
#         model = models.Perawatan
#         fields = [
#             'keterangan_perbaikan',
#         ]
#         labels = {
#             'keterangan_perbaikan': 'Keterangan',
#         }
#         widgets = {
#             'keterangan_perbaikan': forms.Textarea(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#         }


# class BreakForm(forms.ModelForm):
#     class Meta:
#         model = models.Istirahat
#         fields = [
#             'jenis_istirahat',
#         ]
#         labels = {
#             'jenis_istirahat': 'Jenis Break',
#         }
#         widgets = {
#             'jenis_istirahat': forms.Select(
#                 attrs={
#                     'class': 'form-select'
#                 }
#             ),
#         }
#

class IstirahatForm(forms.ModelForm):
    class Meta:
        model = models.Istirahat
        fields = [
            # 'tanggal',
            'waktu_awal',
            'waktu_akhir'
        ]
        labels = {
            'tanggal': 'Tanggal',
            'waktu_awal': 'Jam Istirahat',
            'waktu_akhir': ''
        }
        widgets = {
            'tanggal': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'waktu_awal': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
            'waktu_akhir': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
        }


class PerawatanForm(forms.ModelForm):
    class Meta:
        model = models.Perawatan
        fields = [
            'mesin',
            'is_usable',
            'keterangan_perawatan',
            'tanggal_perawatan',
            'waktu_awal',
            'waktu_akhir'
        ]
        labels = {
            'mesin': 'Mesin',
            'keterangan_perawatan': 'Keterangan',
            'is_usable': 'Apakah mesin masih bisa digunakan?',
            'tanggal_perawatan': 'Tanggal',
            'waktu_awal': 'Waktu Awal',
            'waktu_akhir': 'Waktu Akhir'

        }
        widgets = {
            'mesin': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'keterangan_perawatan': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'is_usable': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'tanggal_perawatan': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'waktu_awal': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
            'waktu_akhir': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
        }


# class LiburForm(forms.ModelForm):
#     class Meta:
#         model = models.Istirahat
#         fields = [
#             'tanggal',
#         ]
#         labels = {
#             'tanggal': 'Tanggal Hari Libur',
#         }
#         widgets = {
#             'tanggal': forms.DateTimeInput(
#                 attrs={
#                     'type': 'date',
#                     'class': 'form-control'
#                 }
#             ),
#         }
