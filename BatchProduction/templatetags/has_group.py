from django import template
import datetime
from JadwalBatchProduction import models
from django.db.models import Count

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='in_mesin')
def in_mesin(datajadwal, mesin):
    return datajadwal.filter(mesin=mesin)


@register.filter(name='index')
def index(indexable, i):
    return indexable[i]


@register.filter(expects_localtime=True)
def parse_iso(value):
    return datetime.datetime.strptime(value, "%Y-%m-%d")


@register.filter(name='countdies')
def countdies(dies, values):
    return models.Jadwal.objects.filter(id_tp=values, dies=dies).count()


@register.filter(name='countdiesmgg')
def countdiesmgg(dies, values):
    return models.Jadwal.objects.filter(tanggal_mulai__week=values, dies=dies).count()


@register.filter(name='countdiesbln')
def countdiesbln(dies, values):
    return models.Jadwal.objects.filter(tanggal_mulai__month=values, dies=dies).count()


@register.filter(name='countdiesthn')
def countdiesthn(dies, values):
    return models.Jadwal.objects.filter(tanggal_mulai__year=values, dies=dies).count()