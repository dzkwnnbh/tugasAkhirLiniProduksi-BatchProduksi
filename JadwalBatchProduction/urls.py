from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.produksi, name='produksiBatchProduction'),
    path('jadwal', views.jadwal, name='jadwal_produksiBatchProduction'),
    path('start/<str:tanggal>', views.mulai_produksi, name='mulai_produksiBatchProduction'),
    path('listjadwal/<str:id_materials>', views.jadwal_produksi, name='listjadwal_produksiBatchProduction'),
    path('listjadwal/jadwal/start/<str:id_jadwal>', views.start_produksi, name='mulai_jadwalproduksiBatchProduction'),
    path('listjadwal/jadwal/stop/<str:id_jadwal>', views.stop_produksi, name='selesai_jadwalproduksiBatchProduction'),
    path('istirahat/<str:tanggal>', views.data_istirahat, name='istirahat_BatchProduction'),
    path('istirahat/<str:tanggal>/add/istirahat', views.tambah_istirahat, name='tambah_istirahatBatchProduction'),
    path('istirahat/hapus/<str:pk>', views.hapus_istirahat, name='hapus_istirahatBatchProduction'),
    path('add/tahunan', views.tambah_targettahunan, name='tambah_targettahunanBatchProduction'),
    path('remove/tahunan/<str:id_target>', views.hapus_targettahunan, name='hapus_targettahunanBatchProduction'),
    path('edit/tahunan/<str:id_target>', views.edit_targettahunan, name='edit_targettahunanBatchProduction'),
    path('add/bulanan', views.tambah_targetbulanan, name='tambah_targetbulananBatchProduction'),
    path('remove/bulanan/<str:id_target>', views.hapus_targetbulanan, name='hapus_targetbulananBatchProduction'),
    path('edit/bulanan/<str:id_target>', views.edit_targetbulanan, name='edit_targetbulananBatchProduction'),
    path('add/mingguan', views.tambah_targetmingguan, name='tambah_targetmingguanBatchProduction'),
    path('remove/mingguan/<str:id_target>', views.hapus_targetmingguan, name='hapus_targetmingguanBatchProduction'),
    path('edit/mingguan/<str:id_target>', views.edit_targetmingguan, name='edit_targetmingguanBatchProduction'),
    path('add/harian', views.tambah_targetharian, name='tambah_targetharianBatchProduction'),
    path('remove/harian/<str:id_target>', views.hapus_targetharian, name='hapus_targetharianBatchProduction'),
    path('edit/harian/<str:id_target>', views.edit_targetharian, name='edit_targetharianBatchProduction'),
    path('add/libur', views.tambah_libur, name='tambah_liburBatchProduction'),
    path('add/prodsharian/<str:tanggal>', views.tambah_produksiharian, name='tambah_produksiharianBatchProduction'),
    path('remove/prodsharian/<str:id_target>', views.hapus_produksiharian, name='hapus_produksiharianBatchProduction'),
    path('edit/prodsharian/<str:id_target>', views.edit_produksiharian, name='edit_produksiharianBatchProduction'),
    path('dies/penggunaan', views.penggunaan_dies, name='penggunaan_diesBatchProduction')

]
