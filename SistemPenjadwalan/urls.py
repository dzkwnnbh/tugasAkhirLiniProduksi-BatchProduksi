from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import viewsBatchProduction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls','users')),
    path('liniProduksi/', include('liniProduksi.urls','liniProduksi')),
    path('produk/', include('produk.urls','produk')),
    path('jadwal/', include('jadwal.urls','jadwal')),
    path('engineeringOrder/', include('engineeringOrder.urls','engineeringOrder')),
    path('contributor/',views.contributor, name='contributor'),
    path('home/',views.home, name='home'),
    path('', views.index, name='index'),
    path('batch/about/', viewsBatchProduction.about, name='about'),
    path('batch/about/&', viewsBatchProduction.dz, name='dz'),
    path('login/', viewsBatchProduction.loginview, name='login'),
    path('logout/', viewsBatchProduction.logoutview, name='logout'),
    path('plant/', viewsBatchProduction.plant, name='plant'),
    path('batch/', include('BatchProduction.urls'), name='batch'),
    path('<slug:instance>/', viewsBatchProduction.notfound, name='404'),
    # path('', viewsBatchProduction.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)