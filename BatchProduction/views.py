from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from JadwalBatchProduction import models as models_jadwal


@login_required(redirect_field_name='', login_url='/login')
def index(request):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Index',
    }

    return render(request, 'BatchProduction/managerBatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def mesin(request):
    datamesin = models.Mesin.objects.all().order_by('id_mesin')

    context = {
        'judul': 'Batch Production',
        'subjudul': 'Mesin',
        'datamesin': datamesin,
    }
    return render(request, 'BatchProduction/mesinBatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_mesin(request):
    input_form = forms.MesinForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Tambah Mesin',
        'header': 'Tambah Stasiun Kerja & Mesin',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                if not models.Mesin.objects.filter(id_mesin=input_form.cleaned_data.get('id_mesin')).exists():
                    input_form.save()
                    return redirect("mesinBatchProduction")
                else:
                    context = {
                        'judul': 'Batch Production',
                        'subjudul': 'Error',
                        'error': 'ID Mesin Sudah Ada',
                        'isi': 'ID Mesin sudah ada. '
                               'Silakan <a href="/manager/mesin">kembali</a>.'
                    }
                    return render(request, '404.html', context)
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_mesin(request, id_mesin):
    mesin_update = models.Mesin.objects.get(id_mesin=id_mesin)
    input_form = forms.MesinForm(request.POST or None, instance=mesin_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Mesin',
        'header': 'Edit Mesin',
        'id': id_mesin,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("mesinBatchProduction")
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_mesin(request, id_mesin):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Mesin',
        'header': 'Hapus Mesin',
        'id': id_mesin,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.Mesin.objects.filter(id_mesin=id_mesin).delete()
            return redirect('mesinBatchProduction')

        return render(request, 'BatchProduction/delete_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_operator(request):
    input_form = forms.OperatorSKForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Tambah Operator',
        'header': 'Tambah Operator',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                if not models.OperatorSK.objects.filter(username=input_form.cleaned_data.get('username')).exists():
                    input_form.save()
                    return redirect("mesinBatchProduction")
                else:
                    context = {
                        'judul': 'Batch Production',
                        'subjudul': 'Error',
                        'error': 'Username Sudah Ada',
                        'isi': 'Username sudah ada. '
                               'Silakan <a href="/manager/mesin">kembali</a>.'
                    }
                    return render(request, '404.html', context)
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_operator(request, username):
    mesin_update = models.OperatorSK.objects.get(id_mesin=id_mesin)
    input_form = forms.OperatorSKForm(request.POST or None, instance=mesin_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Operator',
        'header': 'Edit Operator',
        'id': username,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("mesinBatchProduction")
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_operator(request, username):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Operator',
        'header': 'Hapus Operator',
        'id': username,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.OperatorSK.objects.filter(username=username).delete()
            return redirect('mesinBatchProduction')
        return render(request, 'BatchProduction/delete_BatchProduction.html', context)
#
#
# @login_required(redirect_field_name='', login_url='/login')
# def detail_mesin(request, id_mesin):
#     dataproses = models.Proses.objects.filter(mesin_id=id_mesin).order_by('id_proses')
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Detail Proses Mesin',
#         'id': id_mesin,
#         'dataproses': dataproses,
#     }
#     return render(request, 'BatchProduction/detail_mesinBatchProduction.html', context)
#
#
# @login_required(redirect_field_name='', login_url='/login')
# def status_mesin(request, id_mesin):
#     if models.Mesin.objects.get(id_mesin=id_mesin).status_mesin == 1:
#         models.Mesin.objects.filter(id_mesin=id_mesin).update(
#             status_mesin=0
#         )
#     else:
#         models.Mesin.objects.filter(id_mesin=id_mesin).update(
#             status_mesin=1
#         )
#     return redirect('mesinBatchProduction')


@login_required(redirect_field_name='', login_url='/login')
def tambah_proses(request):
    input_form = forms.ProsesForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Tambah Proses',
        'header': 'Tambah Proses',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                if not models.Proses.objects.filter(id_proses=input_form.cleaned_data.get('id_proses')).exists():
                    input_form.save()
                    return redirect("mesinBatchProduction")
                else:
                    context = {
                        'judul': 'Batch Production',
                        'subjudul': 'Error',
                        'error': 'ID Proses Sudah Ada',
                        'isi': 'ID Proses sudah ada. '
                               'Silakan <a href="/manager/mesin">kembali</a>.'
                    }
                    return render(request, '404.html', context)
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_proses(request, id_proses):
    proses_update = models.Proses.objects.get(id_proses=id_proses)
    input_form = forms.ProsesForm(request.POST or None, instance=proses_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Proses',
        'header': 'Edit Proses',
        'id': id_proses,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("mesinBatchProduction")
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_proses(request, id_proses):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Proses',
        'header': 'Hapus Proses',
        'id': id_proses,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.Proses.objects.filter(id_proses=id_proses).delete()
            return redirect('mesinBatchProduction')

        return render(request, 'BatchProduction/delete_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_dies(request):
    input_form = forms.DiesForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Tambah Dies',
        'header': 'Tambah Dies',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                if not models.Dies.objects.filter(id_dies=input_form.cleaned_data.get('id_dies')).exists():
                    input_form.save()
                    return redirect("mesinBatchProduction")
                else:
                    context = {
                        'judul': 'Batch Production',
                        'subjudul': 'Error',
                        'error': 'ID Dies Sudah Ada',
                        'isi': 'ID Dies sudah ada. '
                               'Silakan <a href="/manager/mesin">kembali</a>.'
                    }
                    return render(request, '404.html', context)
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_dies(request, id_dies):
    dies_update = models.Dies.objects.get(id_dies=id_dies)
    input_form = forms.DiesForm(request.POST or None, instance=dies_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Dies',
        'header': 'Edit Dies',
        'id': id_dies,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("mesinBatchProduction")
        return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_dies(request, id_dies):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Dies',
        'header': 'Hapus Dies',
        'id': id_dies,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.Dies.objects.filter(id_dies=id_dies).delete()
            return redirect('mesinBatchProduction')

        return render(request, 'BatchProduction/delete_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_istirahat(request):
    input_form = forms.IstirahatForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Tambah Istirahat',
        'header': 'Tambah Istirahat Produksi ',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                models.Istirahat.objects.create(
                    waktu_awal=request.POST.get('waktu_awal'),
                    waktu_akhir=request.POST.get('waktu_akhir'),
                    mesin=models.Mesin.objects.get(id_mesin=request.POST.get('mesin'))
                )
                return redirect('mesin_BatchProduction')
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_istirahat(request, pk):
    id_prodsharian = models.Istirahat.objects.get(pk=pk).id_prodsharian_id
    models.Istirahat.objects.filter(id=pk).delete()
    return redirect('istirahat_BatchProduction', mesin=id_prodsharian)


# @login_required(redirect_field_name='', login_url='/login')
# def perawatan(request):
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Data Perawatan',
#         'header': 'Data Perawatan',
#         'kerusakan': models.Perawatan.objects.all(),
#         # 'diperbaiki': models.Perawatan.objects.filter(is_fixed=True)
#     }
#
#     return render(request, "BatchProduction/perawatan_mesinBatchProduction.html", context)
#
#
# @login_required(redirect_field_name='', login_url='/login')
# def tambah_perawatan(request):
#     input_form = forms.PerawatanForm(request.POST or None)
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Lapor Perawatan',
#         'header': 'Lapor Perawatan',
#         'input_form': input_form,
#     }
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if input_form.is_valid():
#                 if request.POST.get('is_usable') == '0':
#                     models.Istirahat.objects.create(
#                         mesin=models.Mesin.objects.get(id_mesin=request.POST.get('mesin')),
#                         waktu_awal=request.POST.get('waktu_awal'),
#                         waktu_akhir=request.POST.get('waktu_akhir')
#                     )
#                 input_form.save()
#                 return redirect("perawatanBatchProduction")
#         return render(request, "BatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def detail_mesin(request, id_mesin):
    dataproses = models.Proses.objects.filter(mesin_id=id_mesin).order_by('id_proses')
    datarusak = models_jadwal.Perawatan.objects.filter(mesin_id=id_mesin).order_by('tanggal_perawatan')
    dataoperator = models.OperatorSK.objects.filter(lokasi=models.Mesin.objects.get(id_mesin=id_mesin).stasiunkerja_ptr_id)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Detail Mesin',
        'id': id_mesin,
        'dataproses': dataproses,
        'datarusak': datarusak,
        'dataoperator': dataoperator
    }
    return render(request, 'BatchProduction/detail_mesinBatchProduction.html', context)
