import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Min, Max
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware
from . import forms, models
from .batch_getter import get_batch
from BatchProduction.models import Mesin, Proses, Dies, StasiunKerja, OperatorSK
from produk.models import Material, Varian


@login_required(redirect_field_name='', login_url='/login')
def produksi(request):
    targettahunan = models.TargetTahunan.objects.all()
    targetbulanan = models.TargetBulanan.objects.all()
    targetmingguan = models.TargetMingguan.objects.all()
    targetharian = models.TargetHarian.objects.all().order_by('-tanggal')
    produksiharian = models.ProduksiHarian.objects.all()
    sekarang = datetime.datetime.today()
    hariini = targetharian.filter(tanggal=sekarang)
    produksisekarang = produksiharian.filter(tanggal=sekarang)
    # if hariini:
    #     mngg = str(hariini[0].minggu)
    #     awal = datetime.datetime.strptime(str(datetime.datetime.now().isocalendar()[0]) + '-' + mngg + '-1', "%Y-%W-%w")
    # else:
    #     awal = datetime.datetime.now()

    context = {
        'judul': 'Schedule Management',
        'subjudul': 'Target Produksi',
        'targettahunan': targettahunan,
        'targetbulanan': targetbulanan,
        'targetmingguan': targetmingguan,
        'targetharian': targetharian,
        'produksiharian': produksiharian,
        'hariini': hariini,
        'produksisekarang': produksisekarang,
        'sekarang': sekarang,
        # 'awal': awal,
        # 'akhir': awal + datetime.timedelta(days=4)
    }
    return render(request, 'JadwalBatchProduction/produksiBatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def jadwal(request):
    if not request.user.groups.filter(name__in='Produksi').exists:
        return redirect('produksiBatchProduction')

    berjalan = models.TargetHarian.objects.filter(tanggal=datetime.datetime.now())
    selesai = models.TargetHarian.objects.filter(tanggal__lt=datetime.datetime.now())

    context = {
        'judul': 'Schedule Management',
        'subjudul': 'JadwalBatchProduction Operasi',
        'berjalan': berjalan,
        'selesai': selesai,
    }
    return render(request, 'JadwalBatchProduction/jadwal_produksiBatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_targettahunan(request):
    input_form = forms.TargetTahunanForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Buat Target Tahunan',
        'header': 'Buat Target Tahunan',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            var = request.POST.get('material')
            matdata = Material.objects.filter(varian=var, dies_id__isnull=False, is_berlaku=1).values_list(
                'idMaterial', flat=True).distinct()
            mat = list(matdata)
            jml = [Material.objects.filter(varian=var, idMaterial=x).count() * int(request.POST.get('target')) for x in matdata]
            # asd=asdd
            for material in range(len(mat)):
                models.TargetTahunan.objects.create(
                    tahun=request.POST.get('tahun'),
                    material=mat[material],
                    target=jml[material],
                )
            return redirect("produksiBatchProduction")

        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    #         if input_form.is_valid():
    #             input_form.save()
    #             return redirect("produksiBatchProduction")
    #
    #     return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_targettahunan(request, id_target):
    targetproduksi_update = models.TargetTahunan.objects.get(id=id_target)
    input_form = forms.TargetTahunanForm(request.POST or None, instance=targetproduksi_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Target Tahunan',
        'header': 'Edit Target Tahunan',
        'id': id_target,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_targettahunan(request, id_target):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Target Tahunan',
        'header': 'Hapus Target Tahunan',
        'id': id_target,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.TargetTahunan.objects.filter(id=id_target).delete()
            return redirect('produksiBatchProduction')

        return render(request, 'JadwalBatchProduction/delete_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_targetbulanan(request):
    input_form = forms.TargetBulananForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Buat Target Bulanan',
        'header': 'Buat Target Bulanan',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            var = request.POST.get('material')
            matdata = Material.objects.filter(varian=var, dies_id__isnull=False, is_berlaku=1).values_list(
                'idMaterial', flat=True).distinct()
            mat = list(matdata)
            jml = [Material.objects.filter(varian=var, idMaterial=x).count() * int(request.POST.get('target')) for x in matdata]
            # asd=asdd
            for material in range(len(mat)):
                models.TargetBulanan.objects.create(
                    tahun=request.POST.get('tahun'),
                    bulan=request.POST.get('bulan'),
                    material=mat[material],
                    target=jml[material],
                )
            return redirect("produksiBatchProduction")

        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_targetbulanan(request, id_target):
    targetproduksi_update = models.TargetBulanan.objects.get(id=id_target)
    input_form = forms.TargetBulananForm(request.POST or None, instance=targetproduksi_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Target Bulanan',
        'header': 'Edit Target Bulanan',
        'id': id_target,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_targetbulanan(request, id_target):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Target Bulanan',
        'header': 'Hapus Target Bulanan',
        'id': id_target,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.TargetBulanan.objects.filter(id=id_target).delete()
            return redirect('produksiBatchProduction')

        return render(request, 'JadwalBatchProduction/delete_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_targetmingguan(request):
    input_form = forms.TargetMingguanForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Buat Target Mingguan',
        'header': 'Buat Target Mingguan',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            var = request.POST.get('material')
            matdata = Material.objects.filter(varian=var, dies_id__isnull=False, is_berlaku=1).values_list(
                'idMaterial', flat=True).distinct()
            mat = list(matdata)
            jml = [Material.objects.filter(varian=var, idMaterial=x).count() * int(request.POST.get('target')) for x in matdata]
            # asd=asdd
            for material in range(len(mat)):
                models.TargetMingguan.objects.create(
                    tahun=request.POST.get('tahun'),
                    minggu=request.POST.get('minggu'),
                    material=mat[material],
                    target=jml[material],
                )
            return redirect("produksiBatchProduction")

        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_targetmingguan(request, id_target):
    targetproduksi_update = models.TargetMingguan.objects.get(id=id_target)
    input_form = forms.TargetMingguanForm(request.POST or None, instance=targetproduksi_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Target Mingguan',
        'header': 'Edit Target Mingguan',
        'id': id_target,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_targetmingguan(request, id_target):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Target Mingguan',
        'header': 'Hapus Target Mingguan',
        'id': id_target,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.TargetMingguan.objects.filter(id=id_target).delete()
            return redirect('produksiBatchProduction')

        return render(request, 'JadwalBatchProduction/delete_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_targetharian(request):
    input_form = forms.TargetHarianForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Buat Target Harian',
        'header': 'Buat Target Harian',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)

    # models.TargetHarian.objects.create(
    #     tanggal=datetime.datetime.now(tz=pytz.timezone('Asia/Jakarta'))
    # )
    # return redirect('produksiBatchProduction')


@login_required(redirect_field_name='', login_url='/login')
def edit_targetharian(request, id_target):
    targetproduksi_update = models.TargetHarian.objects.get(id=id_target)
    input_form = forms.TargetHarianForm(request.POST or None, instance=targetproduksi_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Target Harian',
        'header': 'Edit Target Harian',
        'id': id_target,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_targetharian(request, id_target):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Target Harian',
        'header': 'Hapus Target Harian',
        'id': id_target,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.TargetHarian.objects.filter(id=id_target).delete()
            return redirect('produksiBatchProduction')

        return render(request, 'JadwalBatchProduction/delete_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_produksiharian(request, tanggal):
    input_form = forms.ProduksiHarianForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Buat Produksi Harian',
        'header': 'Buat Produksi Harian',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            var = request.POST.get('material')
            matdata = Material.objects.filter(varian=var, dies_id__isnull=False, is_berlaku=1).values_list(
                'idMaterial', flat=True).annotate(jumlah=Count('idMaterial')).order_by('jumlah').distinct()
            mat_input = list(matdata)
            jml_input = [Material.objects.filter(varian=var, idMaterial=x).count() * int(request.POST.get('target')) for x in mat_input]
            # jika ada komponen sama dan digabung
            if models.ProduksiHarian.objects.filter(tanggal=tanggal, material__in=mat_input).exists() and models.TargetHarian.objects.get(tanggal=tanggal).is_digabung == 'Gabung':
                # list komponen yang sudah ada
                mat_exist = list(models.ProduksiHarian.objects.filter(tanggal=tanggal).values_list('material', flat=True))
                data_mat_exist = mat_exist
                # list target komponen yang sudah ada
                jml_exist = list(models.ProduksiHarian.objects.filter(tanggal=tanggal).values_list('target', flat=True))
                # list komponen yang sama
                mat_yg_sama = []
                for a in mat_input:
                    for b in mat_exist:
                        if b == a:
                            mat_yg_sama.append(b)
                # setiap komponen yang sama
                for c in mat_yg_sama:
                    # hitung target setelah dijumlah
                    total_c = models.ProduksiHarian.objects.get(tanggal=tanggal, material=c).target + Material.objects.filter(varian=var, idMaterial=c).count() * int(request.POST.get('target'))
                    # pindah komponen ke awal
                    mat_input.insert(0, mat_input.pop(mat_input.index(str(c))))
                    # hapus komponen yang sudah ada
                    del jml_exist[mat_exist.index(str(c))]
                    mat_exist.remove(str(c))
                    # masukkan list baru setelah dijumlah targetnya
                    jml_input = [Material.objects.filter(varian=var, idMaterial=x).count() * int(request.POST.get('target')) for x in mat_input]
                    jml_input[mat_input.index(str(c))] = total_c
                # buat list keseluruhan (yang sudah ada dan yang dimasukkan)
                for mats in mat_input:
                    mat_exist.append(mats)
                for jmlh in jml_input:
                    jml_exist.append(jmlh)
                mat_input = mat_exist
                jml_input = jml_exist
                # hapus data yang sudah ada
                models.ProduksiHarian.objects.filter(tanggal=tanggal, material__in=data_mat_exist).delete()
            # asd=asdd
            for material in range(len(mat_input)):
                models.ProduksiHarian.objects.create(
                    material=mat_input[material],
                    target=jml_input[material],
                    tanggal=tanggal,
                )
            return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def edit_produksiharian(request, id_target):
    targetproduksi_update = models.ProduksiHarian.objects.get(id=id_target)
    input_form = forms.ProduksiHarianForm(request.POST or None, instance=targetproduksi_update)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Edit Produksi Harian',
        'header': 'Edit Produksi Harian',
        'id': id_target,
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                input_form.save()
                return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_produksiharian(request, id_target):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Hapus Produksi Harian',
        'header': 'Hapus Produksi Harian',
        'id': models.ProduksiHarian.objects.get(id=id_target).tanggal,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            models.ProduksiHarian.objects.filter(id=id_target).delete()
            return redirect('produksiBatchProduction')

        return render(request, 'JadwalBatchProduction/delete_BatchProduction.html', context)


# @login_required(redirect_field_name='', login_url='/login')
# def tambah_targetproduksi(request):
#     input_form = forms.TargetProduksiForm(request.POST or None)
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Buat Target Produksi',
#         'header': 'Buat Target Produksi',
#         'input_form': input_form,
#     }
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if input_form.is_valid():
#                 if not models.ProduksiHarian.objects.filter(varian=input_form.cleaned_data.get('varian'),
#                                                             status='Dibuat').exists():
#                     input_form.save()
#                     return redirect("produksiBatchProduction")
#                 else:
#                     context = {
#                         'judul': 'Batch Production',
#                         'subjudul': 'Error',
#                         'error': 'ID Sudah ada',
#                         'isi': 'ID Material sudah ada. Silakan',
#                         'link': '/batch/produksi',
#                         'link_txt': 'kembali'
#                     }
#                     return render(request, '404.html', context)
#         return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)
#
#
# @login_required(redirect_field_name='', login_url='/login')
# def edit_targetproduksi(request, id_target):
#     targetproduksi_update = models.ProduksiHarian.objects.get(id=id_target)
#     input_form = forms.TargetProduksiForm(request.POST or None, instance=targetproduksi_update)
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Edit Target Produksi',
#         'header': 'Edit Target Produksi',
#         'id': id_target,
#         'input_form': input_form,
#     }
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if input_form.is_valid():
#                 input_form.save()
#                 return redirect("produksiBatchProduction")
#         return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)
#
#
# @login_required(redirect_field_name='', login_url='/login')
# def hapus_targetproduksi(request, id_target):
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Hapus Target Produksi',
#         'header': 'Hapus Target Produksi',
#         'id': id_target,
#     }
#
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             models.ProduksiHarian.objects.filter(id=id_target).delete()
#             return redirect('produksiBatchProduction')
#
#         return render(request, 'JadwalBatchProduction/delete_BatchProduction.html', context)


# @login_required(redirect_field_name='', login_url='/login')
# def tambah_break(request, id_prodsharian):
#     input_form = forms.BreakForm(request.POST or None)
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Tambah Break',
#         'header': 'Tambah Break',
#         'input_form': input_form,
#     }
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if input_form.is_valid():
#                 if input_form.cleaned_data.get('jenis_break') == 'Istirahat':
#                     return redirect('tambah_istirahatBatchProduction', id_prodsharian=id_prodsharian)
#                 elif input_form.cleaned_data.get('jenis_break') == 'Libur':
#                     return redirect('tambah_liburBatchProduction', id_prodsharian=id_prodsharian)
#         return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_libur(request):
    input_form = forms.TargetHarianForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Buat Target Harian',
        'header': 'Buat Target Harian',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            models.TargetHarian.objects.create(
                tanggal=request.POST.get('tanggal'),
                is_libur=True
            )
            return redirect("produksiBatchProduction")
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


# @login_required(redirect_field_name='', login_url='/login')
# def tambah_libur(request, id_prodsharian):
#     input_form = forms.LiburForm(request.POST or None)
#     produksian = models.ProduksiHarian.objects.get(id=id_prodsharian).tanggal
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Tambah Libur',
#         'header': 'Tambah Libur Produksi ' + produksian.strftime("%d/%m/%Y"),
#         'input_form': input_form,
#     }
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if input_form.is_valid():
#                 models.Break.objects.create(
#                     id_prodsharian=models.ProduksiHarian.objects.get(id=id_prodsharian),
#                     jenis_break='Libur',
#                     tanggal=request.POST.get('tanggal'),
#                 )
#                 return redirect('break_produksiBatchProduction', id_prodsharian=id_prodsharian)
#         return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


def mulai_produksi(request, tanggal):
    if not models.ProduksiHarian.objects.filter(tanggal=tanggal).exists():
        context = {
            'judul': 'Batch Production',
            'subjudul': 'Error',
            'error': 'No Production',
            'isi': 'Tidak ada produksi yang dimulai. Silakan ',
            'link': '/batch/produksi',
            'link_txt': 'kembali dan perbaiki target produksi'
        }
        return render(request, '404.html', context)
    hari_kerja = 1
    data_material = []
    for i in models.ProduksiHarian.objects.filter(tanggal=tanggal).values_list('material', flat=True):
        data_material.append(Material.objects.filter(idMaterial=i)[0])

    list_dies = [xxx.dies_id for xxx in data_material]
    list_dies = list(dict.fromkeys(list_dies))
    list_proses = list(Dies.objects.filter(id_dies__in=list_dies).values_list('proses_id', flat=True).distinct())
    list_mesin = [Proses.objects.get(id_proses=proses).mesin_id for proses in list_proses]
    # for proses in list_proses:
    #     mesin =
    #     for ms in mesin:
    #         if Mesin.objects.get(id_mesin=ms).status_mesin == 1:
    #         list_mesin.append(ms)
    #             break
    #         else:
    #             context = {
    #                 'judul': 'Batch Production',
    #                 'subjudul': 'Error',
    #                 'error': 'Mesin Tidak Tersedia',
    #                 'isi': 'Ada mesin yang tidak tersedia untuk produksi ini. Silakan',
    #                 'link': '/batch/mesin',
    #                 'link_txt': 'cek mesin'
    #             }
    #             return render(request, '404.html', context)
    list_mesin = list(dict.fromkeys(list_mesin))

    # Pembuatan jadwal di tiap stasiun kerja
    for i in list_mesin:
        # Buka data material penyusun varian di mesin i
        material_i = []
        for x in data_material:
            if Material.objects.get(id=x.id).dies.proses.mesin_id == i:
                material_i.append(x)
        data_material_i = material_i
        matmat = list(models.ProduksiHarian.objects.filter(tanggal=tanggal).values_list('material', flat=True))
        # Pencarian durasi produksi mesin i
        durasi_produksi = max([a.dies.proses.durasiProduksi for a in data_material_i])

        # Pencarian durasi setup dies di mesin i
        list_dies = [xxx.dies_id for xxx in data_material_i]
        durasi_setup = max([Dies.objects.get(id_dies=die).durasi_setup for die in list_dies])

        # Pencarian data produksi di mesin i
        data_produksi = list(models.ProduksiHarian.objects.filter(tanggal=tanggal).values_list('target', flat=True))

        # Pencarian jam kerja di mesin i
        stasiun_kerja = Mesin.objects.get(id_mesin=i).stasiunkerja_ptr_id
        mulai_kerja = StasiunKerja.objects.get(id=stasiun_kerja).mulai_kerja
        selesai_kerja = StasiunKerja.objects.get(id=stasiun_kerja).selesai_kerja
        date = datetime.date(1, 1, 1)
        jam_kerja = (datetime.datetime.combine(date, selesai_kerja) - datetime.datetime.combine(date, mulai_kerja)).seconds / 60
        # asd=asdd
        # Jika jam kerja kurang dari jam produksi total, batal
        if sum(data_produksi)*durasi_produksi > hari_kerja*jam_kerja:
            context = {
                'judul': 'Batch Production',
                'subjudul': 'Error',
                'error': 'Overcapacity',
                'isi': 'Produksi melebihi kapasitas. Silakan',
                'link': '/batch/produksi',
                'link_txt': 'kembali dan perbaiki target produksi'
            }
            return render(request, '404.html', context)
        if (jam_kerja * hari_kerja - sum(data_produksi) * durasi_produksi) // durasi_setup // hari_kerja < 1:
            context = {
                'judul': 'Batch Production',
                'subjudul': 'Error',
                'error': 'Overcapacity',
                'isi': 'Produksi melebihi kapasitas. Silakan',
                'link': '/batch/produksi',
                'link_txt': 'kembali dan perbaiki target produksi'
            }
            return render(request, '404.html', context)
        # Pencarian batch dengan algoritma
        batch = get_batch(hari_kerja, durasi_produksi, durasi_setup, data_produksi, jam_kerja)
        # batch_min = [Material.objects.filter(idMaterial=mat).count() for mat in data_material_i]

        # pembuatan grafik
        # produksi_sehari = (jam_kerja-((jam_kerja*hari_kerja-sum(data_produksi)*durasi_produksi)//durasi_setup//hari_kerja)*durasi_setup)//durasi_produksi
        # tglmulai = datetime.datetime.strptime(tanggal, '%Y-%m-%d')
        # tglmulai_n_jammulai = datetime.datetime.combine(tglmulai,
        #                                                 StasiunKerja.objects.get(id=stasiun_kerja).mulai_kerja)
        # ist_awal = list(
        #     Istirahat.objects.filter(mesin=Mesin.objects.get(id_mesin=i)).values_list('waktu_awal', flat=True))
        # ist_akhir = list(
        #     Istirahat.objects.filter(mesin=Mesin.objects.get(id_mesin=i)).values_list('waktu_akhir', flat=True))
        # a = 0
        # p = 0
        # q = 0
        # jenis = 0
        # istirahat_awal = []
        # istirahat_akhir = []
        # # asd = asdd
        # inputgrafik = []
        # for x in range(sum(data_produksi)):
        #     for yy in range(len(ist_awal)):
        #         istirahat_awal.append(datetime.datetime.combine(tglmulai, ist_awal[yy]))
        #         istirahat_akhir.append(datetime.datetime.combine(tglmulai, ist_akhir[yy]))
        #     for yyy in range(len(istirahat_awal)):
        #         if istirahat_akhir[yyy] >= tglmulai_n_jammulai >= istirahat_awal[yyy] or istirahat_akhir[yyy] >= tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_produksi) >= istirahat_awal[yyy]:
        #             koreksi = istirahat_akhir[yyy] - tglmulai_n_jammulai
        #             tglmulai_n_jammulai += koreksi
        #
        #     p += 1
        #     q += 1
        #     datamatt = list(Material.objects.filter(idMaterial=matmat[a]).values_list('id', flat=True))[0]
        #     datamat = Material.objects.get(id=datamatt)
        #
        #     inputgrafik.append('{0} {1} {2}'.format(tglmulai_n_jammulai.time(), (tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_produksi)).time(), datamat.idMaterial))
        #     tglmulai_n_jammulai += datetime.timedelta(minutes=durasi_produksi)
        #
        #     if q == batch[jenis]:
        #         jenis += 1
        #         a += 1
        #         q = 0
        #         if p % produksi_sehari != 0:
        #             asdasdasd = tglmulai_n_jammulai.time()
        #             inputgrafik.append('{0} {1} {2}'.format(tglmulai_n_jammulai.time(), (tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_setup)).time(), 'Setup'))
        #         tglmulai_n_jammulai += datetime.timedelta(minutes=durasi_setup)
        #         if jenis > len(batch) - 1:
        #             jenis = 0
        #             a = 0
        #
        # plt.figure(figsize=(24, 5))
        # ax = plt.gca()
        # # plt.gcf().autofmt_xdate()
        # ax.yaxis.set_visible(False)
        # for line in inputgrafik:
        #     datagrafik = line.split()
        #     if datagrafik[2] == 'Setup':
        #         event = datagrafik[2]
        #     else:
        #         event = datagrafik[2] + ' = ' + datagrafik[-1]
        #     # datagrafik = list(map(str, datagrafik))
        #     start = datetime.datetime.strptime(datagrafik[0], '%H:%M:00')
        #     end = datetime.datetime.strptime(datagrafik[1], '%H:%M:00')
        #     if event == 'Setup':
        #         plt.fill_between([start, end], [5, 5], color='yellow', edgecolor='k', linewidth=1)
        #     else:
        #         plt.fill_between([start, end], [5, 5], color='green', edgecolor='k', linewidth=1)
        #
        # ff = BytesIO()
        # plt.savefig(ff, format='png')
        # content_file = ImageFile(ff)
        # # produksi_harian_instance = models.JadwalBatchProduction(id_tp=tanggal)
        # # produksi_harian_instance.grafik.save(str(tanggal)+str(i)+'.png', content_file)
        # # produksi_harian_instance.save()

        # Proses pembuatan jadwal untuk mesin i
        produksi_sehari = (jam_kerja - ((jam_kerja * hari_kerja - sum(data_produksi) * durasi_produksi) // durasi_setup // hari_kerja) * durasi_setup) // durasi_produksi
        tglmulai = datetime.datetime.strptime(tanggal, '%Y-%m-%d')
        tglmulai_n_jammulai = datetime.datetime.combine(tglmulai,
                                                        StasiunKerja.objects.get(id=stasiun_kerja).mulai_kerja)
        ist_awal = list(
            # models.Istirahat.objects.filter(mesin=Mesin.objects.get(id_mesin=i)).values_list('waktu_awal', flat=True))
            models.Istirahat.objects.filter(tanggal=tanggal).values_list('waktu_awal', flat=True))
        ist_akhir = list(
            # models.Istirahat.objects.filter(mesin=Mesin.objects.get(id_mesin=i)).values_list('waktu_akhir', flat=True))
            models.Istirahat.objects.filter(tanggal=tanggal).values_list('waktu_akhir', flat=True))
        a = 0
        p = 0
        q = 0
        jenis = 0
        istirahat_awal = []
        istirahat_akhir = []
        # asd = asdd
        for x in range(sum(data_produksi)):
            for yy in range(len(ist_awal)):
                istirahat_awal.append(datetime.datetime.combine(tglmulai, ist_awal[yy]))
                istirahat_akhir.append(datetime.datetime.combine(tglmulai, ist_akhir[yy]))
            for yyy in range(len(istirahat_awal)):
                if istirahat_akhir[yyy] >= tglmulai_n_jammulai >= istirahat_awal[yyy] or istirahat_akhir[yyy] >= tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_produksi) >= istirahat_awal[yyy]:
                    koreksi = istirahat_akhir[yyy] - tglmulai_n_jammulai
                    tglmulai_n_jammulai += koreksi

            p += 1
            q += 1
            datamatt = list(Material.objects.filter(idMaterial=matmat[a]).values_list('id', flat=True))[0]
            datamat = Material.objects.get(id=datamatt)
            models.Jadwal.objects.create(
                id_tp=tanggal,
                material=datamat.idMaterial,
                mesin=i,
                stasiun_kerja=StasiunKerja.objects.get(id=Mesin.objects.get(
                    id_mesin=i).stasiunkerja_ptr_id).id_stasiun_kerja,
                proses=datamat.dies.proses_id,
                dies=datamat.dies_id,
                tanggal_mulai=make_aware(tglmulai_n_jammulai),
                tanggal_selesai=make_aware(tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_produksi)),
                # grafik=ff
            )

            tglmulai_n_jammulai += datetime.timedelta(minutes=durasi_produksi)

            if q == batch[jenis]:
                jenis += 1
                a += 1
                q = 0
                if p % produksi_sehari != 0:
                    models.Jadwal.objects.create(
                        id_tp=tanggal,
                        # varian=id_target_material,
                        material='Setup',
                        mesin=i,
                        stasiun_kerja=StasiunKerja.objects.get(id=Mesin.objects.get(
                            id_mesin=i).stasiunkerja_ptr_id).id_stasiun_kerja,
                        proses='-',
                        dies='-',
                        tanggal_mulai=make_aware(tglmulai_n_jammulai),
                        tanggal_selesai=make_aware(tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_setup)),
                    )
                tglmulai_n_jammulai += datetime.timedelta(minutes=durasi_setup)
                if jenis > len(batch) - 1:
                    jenis = 0
                    a = 0

    models.TargetHarian.objects.filter(tanggal=tanggal).update(
        is_dijadwal=True,
        waktumulai=make_aware(datetime.datetime.now())
    )

    return redirect('produksiBatchProduction')


@login_required(redirect_field_name='', login_url='/login')
def jadwal_produksi(request, id_materials):
    id_material = models.TargetHarian.objects.get(id=int(id_materials)).tanggal
    # nama = Material.objects.get(id=id_material).varian_id
    prodsjadwalasli = models.Jadwal.objects.filter(id_tp=id_material)
    prodsjadwal = prodsjadwalasli.order_by('tanggal_selesai_asli', 'tanggal_mulai', '-is_go')
    listmesin = list(dict.fromkeys(list(prodsjadwal.values_list('mesin', flat=True))))
    listsk = []

    for mesin in listmesin:
        listsk.append(prodsjadwal.filter(mesin=mesin).values_list('stasiun_kerja', flat=True)[0])
    # asd=asdd
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Jadwal',
        # 'id': nama,
        'datamesin': listmesin,
        'datask': listsk,
        'datajadwalasli': prodsjadwalasli,
        'datajadwal': prodsjadwal
    }
    return render(request, 'JadwalBatchProduction/detail_produksiBatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def start_produksi(request, id_jadwal):
    models.Jadwal.objects.filter(id=id_jadwal).update(
        tanggal_mulai_asli=make_aware(datetime.datetime.now())
    )
    id_tp = models.Jadwal.objects.get(id=id_jadwal).id_tp
    # id_tp = models.JadwalBatchProduction.objects.get(id=id_jadwal).id_tp
    if models.TargetHarian.objects.get(tanggal=id_tp).waktumulai is None:
        models.TargetHarian.objects.filter(id=id_jadwal).update(
            waktumulai=make_aware(datetime.datetime.now()),
        )
    return redirect('listjadwal_produksiBatchProduction',
                    id_materials=models.TargetHarian.objects.get(tanggal=id_tp).id)


@login_required(redirect_field_name='', login_url='/login')
def stop_produksi(request, id_jadwal):
    stripdate = datetime.datetime.strptime(models.Jadwal.objects.get(id=id_jadwal).id_tp, '%Y-%m-%d')
    # asd=asdd
    models.Jadwal.objects.filter(id=id_jadwal).update(
        tanggal_selesai_asli=make_aware(datetime.datetime.now())
    )
    models.ProduksiHarian.objects.filter(tanggal=models.Jadwal.objects.get(id=id_jadwal).id_tp,
                                         material=models.Jadwal.objects.get(id=id_jadwal).material).update(
        selesai=models.ProduksiHarian.objects.get(tanggal=models.Jadwal.objects.get(id=id_jadwal).id_tp,
                                                  material=models.Jadwal.objects.get(id=id_jadwal).material).selesai + 1
    )
    models.TargetMingguan.objects.filter(minggu=stripdate.isocalendar()[1], tahun=stripdate.year,
                                         material=models.Jadwal.objects.get(id=id_jadwal).material).update(
        selesai=models.TargetMingguan.objects.get(minggu=stripdate.isocalendar()[1], tahun=stripdate.year,
                                                  material=models.Jadwal.objects.get(id=id_jadwal).material).selesai + 1
    )
    models.TargetBulanan.objects.filter(bulan=stripdate.month, tahun=stripdate.year,
                                        material=models.Jadwal.objects.get(id=id_jadwal).material).update(
        selesai=models.TargetBulanan.objects.get(bulan=stripdate.month, tahun=stripdate.year,
                                                 material=models.Jadwal.objects.get(id=id_jadwal).material).selesai + 1
    )
    models.TargetTahunan.objects.filter(tahun=stripdate.year,
                                        material=models.Jadwal.objects.get(id=id_jadwal).material).update(
        selesai=models.TargetTahunan.objects.get(tahun=stripdate.year,
                                                 material=models.Jadwal.objects.get(id=id_jadwal).material).selesai + 1
    )
    id_tp = models.Jadwal.objects.get(id=id_jadwal).id_tp
    # id_tp = models.JadwalBatchProduction.objects.get(id=id_jadwal).id_tp
    if not models.Jadwal.objects.filter(id_tp=id_tp,
                                        tanggal_selesai_asli__isnull=True).exists():
        models.TargetHarian.objects.filter(tanggal=id_tp).update(
            waktuselesai=make_aware(datetime.datetime.now()),
        )
    return redirect('listjadwal_produksiBatchProduction',
                    id_materials=models.TargetHarian.objects.get(tanggal=id_tp).id)


@login_required(redirect_field_name='', login_url='/login')
def data_istirahat(request, tanggal):
    # data_libur = models.Break.objects.filter(id_prodsharian=id_prodsharian, jenis_break="Libur")
    # data_istirahat = models.Break.objects.filter(id_prodsharian=id_prodsharian, jenis_break="Istirahat")
    # mesin = Proses.objects.filter(
    #     id_proses__in=Dies.objects.filter(
    #         id_dies__in=Material.objects.filter(
    #             idMaterial__in=models.ProduksiHarian.objects.filter(
    #                 tanggal=tanggal).values_list(
    #                 'material').distinct()).values_list(
    #             'dies').distinct()).values_list(
    #         'proses').distinct()).values_list(
    #     'mesin').distinct()
    # mesins = Mesin.objects.filter(id_mesin__in=mesin)
    # data_istirahats = Istirahat.objects.filter(mesin__in=mesin)
    data_istirahats = models.Istirahat.objects.filter(tanggal=tanggal)
    # id_mat = models.TargetHarian.objects.get(id=id_prodsharian).tanggal
    # asd=asdd
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Data Istirahat',
        'header': 'Tambah Istirahat',
        'idvar': tanggal,
        # 'mesin': mesins,
        # 'data_libur': data_libur,
        'data_istirahat': data_istirahats
    }

    return render(request, 'JadwalBatchProduction/istirahat_produksiBatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def hapus_istirahat(request, pk):
    tanggal = models.Istirahat.objects.get(pk=pk).tanggal
    models.Istirahat.objects.filter(id=pk).delete()
    return redirect('istirahat_BatchProduction', tanggal=tanggal)


@login_required(redirect_field_name='', login_url='/login')
def tambah_istirahat(request, tanggal):
    input_form = forms.IstirahatForm(request.POST or None)
    # produksian = models.ProduksiHarian.objects.get(id=id_prodsharian).tanggal
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
                    # id_prodsharian=models.ProduksiHarian.objects.get(id=id_prodsharian),
                    # jenis_break='Istirahat',
                    waktu_awal=request.POST.get('waktu_awal'),
                    waktu_akhir=request.POST.get('waktu_akhir'),
                    # id_prodsharian_id=id_prodsharian,
                    tanggal=tanggal
                )
                return redirect('istirahat_BatchProduction', tanggal=tanggal)
        return render(request, "JadwalBatchProduction/add_BatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def perawatan(request):
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Data Perawatan',
        'header': 'Data Perawatan',
        'kerusakan': models.Perawatan.objects.all(),
        # 'diperbaiki': models.Perawatan.objects.filter(is_fixed=True)
    }

    return render(request, "BatchProduction/perawatan_mesinBatchProduction.html", context)


@login_required(redirect_field_name='', login_url='/login')
def tambah_perawatan(request):
    input_form = forms.PerawatanForm(request.POST or None)
    context = {
        'judul': 'Batch Production',
        'subjudul': 'Lapor Perawatan',
        'header': 'Lapor Perawatan',
        'input_form': input_form,
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if input_form.is_valid():
                if request.POST.get('is_usable') == '0':
                    models.Istirahat.objects.create(
                        # mesin=models.Mesin.objects.get(id_mesin=request.POST.get('mesin')),
                        tanggal=request.POST.get('tanggal_perawatan'),
                        waktu_awal=request.POST.get('waktu_awal'),
                        waktu_akhir=request.POST.get('waktu_akhir')
                    )
                input_form.save()
                return redirect("perawatanBatchProduction")
        return render(request, "BatchProduction/add_BatchProduction.html", context)
#
#
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
#                         mesin=request.POST.get('mesin'),
#                         waktu_awal=request.POST.get('waktu_awal'),
#                         waktu_akhir=request.POST.get('waktu_akhir')
#                     )
#                 input_form.save()
#                 return redirect("perawatanBatchProduction")
#         return render(request, "BatchProduction/add_BatchProduction.html", context)
#
#
# @login_required(redirect_field_name='', login_url='/login')
# def detail_mesin(request, id_mesin):
#     dataproses = Proses.objects.filter(mesin_id=id_mesin).order_by('id_proses')
#     datarusak = models.Perawatan.objects.filter(mesin_id=id_mesin).order_by('tanggal_perawatan')
#     dataoperator = OperatorSK.objects.filter(lokasi=Mesin.objects.get(id_mesin=id_mesin).stasiunkerja_ptr_id)
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Detail Mesin',
#         'id': id_mesin,
#         'dataproses': dataproses,
#         'datarusak': datarusak,
#         'dataoperator': dataoperator
#     }
#     return render(request, 'BatchProduction/detail_mesinBatchProduction.html', context)


# @login_required(redirect_field_name='', login_url='/login')
# def perbaiki_kerusakan(request, id_kerusakan):
#     input_form = forms.PerbaikanForm(request.POST or None)
#     context = {
#         'judul': 'Batch Production',
#         'subjudul': 'Laporan Perbaikan',
#         'header': 'Laporan Perbaikan',
#         'id': id_kerusakan,
#         'input_form': input_form,
#     }
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             if input_form.is_valid():
#                 idmesin = models.Perawatan.objects.get(id_kerusakan=id_kerusakan).mesin.id_mesin
#                 if models.Perawatan.objects.get(id_kerusakan=id_kerusakan).is_usable == 0:
#                     pemakaimesin = models.JadwalBatchProduction.objects.filter(mesin=idmesin, tanggal_mulai_asli__isnull=True)
#
#                     listtargetprods = list(models.JadwalBatchProduction.objects.filter(mesin=idmesin, tanggal_mulai_asli__isnull=True).values_list('id_tp', flat=True).distinct())
#                     for trgt in listtargetprods:
#                         id_target_material = models.ProduksiHarian.objects.get(id=trgt).varian_id
#                         tgl_mulai = pemakaimesin.aggregate(Min('tanggal_mulai'))['tanggal_mulai__min']
#                         tgl_selesai = pemakaimesin.aggregate(Max('tanggal_selesai'))['tanggal_selesai__max']
#                         hari_kerja = (tgl_selesai - tgl_mulai).days + 1
#                         selisih = datetime.datetime.now(tz=pytz.timezone('Asia/Jakarta'))
#                         tgl_mulai += selisih - tgl_mulai
#                         tgl_selesai += selisih - tgl_selesai
#
#                         libur = list(
#                             models.Break.objects.filter(jenis_break='Libur', id_prodsharian=trgt).values_list('tanggal', flat=True))
#
#                         # Buka data material penyusun varian
#                         # get_varian = Material.objects.get(id=id_target_material).varian_id
#
#                         data_material = models.JadwalBatchProduction.objects.filter(mesin=idmesin, tanggal_mulai_asli__isnull=True).filter(id_tp=trgt).values_list('material', flat=True).distinct()
#
#                         list_dies = list(data_material.values_list('dies', flat=True).distinct())
#                         list_proses = list(
#                             Dies.objects.filter(id_dies__in=list_dies).values_list('proses', flat=True).distinct())
#                         list_mesin = []
#                         for proses in list_proses:
#                             mesin = list(Proses.objects.filter(id_proses=proses).values_list('mesin', flat=True))
#                             for ms in mesin:
#                                 list_mesin.append(ms)
#
#                         list_mesin = list(dict.fromkeys(list_mesin))
#
#                         # Pembuatan jadwal di tiap stasiun kerja
#                         for i in list_mesin:
#                             # Buka data material penyusun varian di mesin i
#                             mtrl = []
#                             for x in list(data_material.values_list('id', flat=True)):
#                                 if models.JadwalBatchProduction.objects.get(id=x).mesin == i:
#                                     mtrl.append(x)
#                             data_material_i = data_material.filter(id__in=mtrl)
#                             materialnya = list(data_material_i.values_list('id', flat=True).annotate(
#                                 jumlah=Count('material')).order_by('jumlah')
#                                                )
#                             matmat = list(data_material_i.annotate(jumlah=Count('material')).order_by('jumlah').values_list(
#                                 'material', flat=True))
#                             # Pencarian durasi produksi mesin i
#
#                             durasi_produksi = Material.objects.filter(idMaterial__in=matmat).aggregate(Max('durasiProduksi'))['durasiProduksi__max']
#
#                             # Pencarian durasi setup dies di mesin i
#                             list_dies = list(data_material_i.values_list('dies', flat=True).distinct())
#                             list_durasi_setup = []
#                             for dies in list_dies:
#                                 durasi = Dies.objects.get(id_dies=dies).durasi_setup
#                                 list_durasi_setup.append(durasi)
#                             durasi_setup = max(list_durasi_setup)
#
#                             # Pencarian data produksi di mesin i
#                             data_produksi = []
#                             for prods in matmat:
#                                 dtdt = models.JadwalBatchProduction.objects.filter(material=prods, mesin=idmesin, tanggal_mulai_asli__isnull=True).filter(id_tp=trgt).count()
#                                 data_produksi.append(dtdt)
#
#                             # Pencarian jam kerja di mesin i
#                             stasiun_kerja = Mesin.objects.get(id_mesin=i).stasiunkerja_ptr_id
#                             mulai_kerja = StasiunKerja.objects.get(id=stasiun_kerja).mulai_kerja
#                             selesai_kerja = StasiunKerja.objects.get(id=stasiun_kerja).selesai_kerja
#                             date = datetime.date(1, 1, 1)
#                             datetime1 = datetime.datetime.combine(date, selesai_kerja)
#                             datetime2 = datetime.datetime.combine(date, mulai_kerja)
#                             jam_kerja = (datetime1 - datetime2).seconds / 60
#
#                             # Jika jam kerja kurang dari jam produksi total, batal
#                             if sum(data_produksi) * durasi_produksi > hari_kerja * jam_kerja:
#                                 context = {
#                                     'judul': 'Batch Production',
#                                     'subjudul': 'Error',
#                                     'error': 'Hari Kerja Kurang',
#                                     'isi': 'Produksi melebihi kapasitas. Silakan',
#                                     'link': '/batch/produksi',
#                                     'link_txt': 'kembali dan perbaiki target produksi'
#                                 }
#                                 return render(request, '404.html', context)
#                             if (jam_kerja * hari_kerja - sum(
#                                     data_produksi) * durasi_produksi) // durasi_setup // hari_kerja < 1:
#                                 context = {
#                                     'judul': 'Batch Production',
#                                     'subjudul': 'Error',
#                                     'error': 'Hari Kerja Kurang',
#                                     'isi': 'Produksi melebihi kapasitas. Silakan',
#                                     'link': '/batch/produksi',
#                                     'link_txt': 'kembali dan perbaiki target produksi'
#                                 }
#                                 return render(request, '404.html', context)
#                             # Pencarian batch dengan algoritma
#                             batch = get_batch(hari_kerja, durasi_produksi, durasi_setup, data_produksi, jam_kerja)
#
#                             pemakaimesin.delete()
#
#                             # Proses pembuatan jadwal untuk mesin i
#                             produksi_sehari = (jam_kerja - ((jam_kerja * hari_kerja - sum(
#                                 data_produksi) * durasi_produksi) // durasi_setup // hari_kerja) * durasi_setup) // durasi_produksi
#                             tglmulai = tgl_mulai
#                             tglmulai_n_jammulai = datetime.datetime.combine(tglmulai,
#                                                                             StasiunKerja.objects.get(
#                                                                                 id=stasiun_kerja).mulai_kerja)
#                             ist_awal = list(
#                                 models.Break.objects.filter(jenis_break='Istirahat', id_prodsharian=trgt).values_list(
#                                     'waktu_awal',
#                                     flat=True))
#                             ist_akhir = list(
#                                 models.Break.objects.filter(jenis_break='Istirahat', id_prodsharian=trgt).values_list(
#                                     'waktu_akhir',
#                                     flat=True))
#                             a = 0
#                             p = 0
#                             q = 0
#                             jenis = 0
#                             istirahat_awal = []
#                             istirahat_akhir = []
#
#                             for x in range(sum(data_produksi)):
#                                 if tglmulai in libur:
#                                     tglmulai += datetime.timedelta(days=1)
#                                 for yy in range(len(ist_awal)):
#                                     istirahat_awal.append(datetime.datetime.combine(tglmulai, ist_awal[yy]))
#                                     istirahat_akhir.append(datetime.datetime.combine(tglmulai, ist_akhir[yy]))
#                                 for yyy in range(len(istirahat_awal)):
#                                     if istirahat_akhir[yyy] >= tglmulai_n_jammulai >= istirahat_awal[yyy] or istirahat_akhir[
#                                         yyy] >= tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_produksi) >= \
#                                             istirahat_awal[yyy]:
#                                         koreksi = istirahat_akhir[yyy] - tglmulai_n_jammulai
#                                         tglmulai_n_jammulai += koreksi
#
#                                 p += 1
#                                 q += 1
#                                 datamatt = list(Material.objects.filter(idMaterial=matmat[a]).values_list('id', flat=True))[0]
#                                 datamat = Material.objects.get(id=datamatt)
#                                 models.JadwalBatchProduction.objects.create(
#                                     id_tp=trgt,
#                                     varian=id_target_material,
#                                     material=datamat.idMaterial,
#                                     mesin=i,
#                                     stasiun_kerja=StasiunKerja.objects.get(id=Mesin.objects.get(
#                                         id_mesin=i).stasiunkerja_ptr_id).id_stasiun_kerja,
#                                     proses=datamat.dies.proses_id,
#                                     dies=datamat.dies_id,
#                                     tanggal_mulai=make_aware(tglmulai_n_jammulai),
#                                     tanggal_selesai=make_aware(
#                                         tglmulai_n_jammulai + datetime.timedelta(minutes=durasi_produksi)),
#                                 )
#
#                                 tglmulai_n_jammulai += datetime.timedelta(minutes=durasi_produksi)
#
#                                 if p % produksi_sehari == 0:
#                                     tglmulai += datetime.timedelta(days=1)
#                                     tglmulai_n_jammulai = datetime.datetime.combine(tglmulai,
#                                                                                     StasiunKerja.objects.get(
#                                                                                         id=stasiun_kerja).mulai_kerja)
#                                 if q == batch[jenis]:
#                                     jenis += 1
#                                     a += 1
#                                     q = 0
#                                     tglmulai_n_jammulai += datetime.timedelta(minutes=durasi_setup)
#                                     if jenis > len(batch) - 1:
#                                         jenis = 0
#                                         a = 0
#
#                 models.Perawatan.objects.filter(id_kerusakan=id_kerusakan).update(
#                     is_fixed=True,
#                     tanggal_diperbaiki=datetime.datetime.now(),
#                     keterangan_perbaikan=input_form.cleaned_data.get('keterangan_perbaikan')
#                 )
#
#                 if not models.Perawatan.objects.filter(mesin=idmesin, is_fixed=False).exists():
#                     Mesin.objects.filter(id_mesin=idmesin).update(
#                         status_mesin=True)
#                     models.JadwalBatchProduction.objects.filter(mesin=idmesin).update(
#                         is_go=True
#                     )
#                 return redirect("kerusakanBatchProduction")
#
#     return render(request, 'JadwalBatchProduction/add_BatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def penggunaan_dies(request):
    datadies = models.Jadwal.objects.exclude(dies='-').order_by('dies')
    harian = models.TargetHarian.objects.all().order_by('-tanggal')
    mingguan = models.TargetMingguan.objects.all().order_by('-minggu')
    bulanan = models.TargetBulanan.objects.all().order_by('-bulan')
    tahunan = models.TargetTahunan.objects.all().order_by('-tahun')

    context = {
        'judul': 'Batch Production',
        'subjudul': 'Data Penggunaan Dies',
        'datadies': datadies,
        'harian': harian,
        'mingguan': mingguan,
        'bulanan': bulanan,
        'tahunan': tahunan

    }
    return render(request, 'JadwalBatchProduction/penggunaan_diesBatchProduction.html', context)
