from django.contrib import admin
from django.urls import path, include
from . import views
from JadwalBatchProduction import views as views_jadwal

urlpatterns = [
    path('', views.index, name='indexBatchProduction'),
    # path('produk/', include('produk.urls', 'produk')),
    path('produksi/', include('JadwalBatchProduction.urls'), name='produksiBatchProduction'),
    path('mesin/', views.mesin, name='mesinBatchProduction'),
    path('mesin/addmesin/', views.tambah_mesin, name='tambah_mesinBatchProduction'),
    path('mesin/editmesin/<str:id_mesin>', views.edit_mesin, name='edit_mesinBatchProduction'),
    path('mesin/removemesin/<str:id_mesin>', views.hapus_mesin, name='hapus_mesinBatchProduction'),
    path('mesin/detailmesin/<str:id_mesin>', views.detail_mesin, name='detail_mesinBatchProduction'),
    path('mesin/addproses/', views.tambah_proses, name='tambah_prosesBatchProduction'),
    path('mesin/editproses/<str:id_proses>', views.edit_proses, name='edit_prosesBatchProduction'),
    path('mesin/removeproses/<str:id_proses>', views.hapus_proses, name='hapus_prosesBatchProduction'),
    path('mesin/adddies', views.tambah_dies, name='tambah_diesBatchProduction'),
    path('mesin/editdies/<str:id_dies>', views.edit_dies, name='edit_diesBatchProduction'),
    path('mesin/removedies/<str:id_dies>', views.hapus_dies, name='hapus_diesBatchProduction'),
    path('mesin/addoperator', views.tambah_operator, name='tambah_operatorBatchProduction'),
    path('mesin/editoperator/<str:username>', views.edit_operator, name='edit_operatorBatchProduction'),
    path('mesin/removeoperator/<str:username>', views.hapus_operator, name='hapus_operatorBatchProduction'),
    path('mesin/perawatan/', views_jadwal.perawatan, name='perawatanBatchProduction'),
    path('mesin/perawatan/add', views_jadwal.tambah_perawatan, name='tambah_perawatanBatchProduction'),
    # path('mesin/istirahat/add', views.tambah_istirahat, name='tambah_istirahatBatchProduction'),
    # path('mesin/istirahat/hapus/<str:pk>', views.hapus_istirahat, name='hapus_istirahatBatchProduction'),

]
