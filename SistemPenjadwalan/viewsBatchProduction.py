from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'judul': 'Schedule Management',
        'subjudul': 'Main Page',
        'logo': 'img/logo.png'
    }
    if request.user.is_authenticated:
        return redirect('indexBatchProduction')
    else:
        return render(request, "indexBatchProduction.html", context)


def loginview(request):
    context = {
        'judul': 'Schedule Management',
        'subjudul': 'Log In',
    }
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('indexBatchProduction')
        else:
            return render(request, "loginBatchProduction.html", context)

    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = authenticate(request, username=un, password=pw)
        if user is not None:
            login(request, user)
            return redirect('indexBatchProduction')

        else:
            return redirect('login')


@login_required(redirect_field_name='', login_url='/login')
def logoutview(request):
    context = {
        'judul': 'Scheduling Management',
        'subjudul': 'Log out?',
    }

    if request.method == 'POST':
        if request.POST["logout"] == "Logout":
            logout(request)
        return redirect('index')

    return render(request, 'logoutBatchProduction.html', context)


@login_required(redirect_field_name='', login_url='/login')
def plant(request):
    context = {
        'judul': 'Scheduling Management',
        'subjudul': 'Plant',
    }
    return render(request, 'plant.html', context)


def about(request):
    context = {
        'judul': 'Schedule Management',
        'subjudul': 'About',
    }

    return render(request, "aboutBatchProduction.html", context)


def dz(request):
    context = {
        'judul': 'dz',
        'subjudul': 'Secret Passage',
    }

    return render(request, "dz.html", context)


def notfound(request, instance):
    context = {
        'judul': 'Schedule Management',
        'subjudul': 'Error /' + instance,
        'error': 'Halaman Tidak Ditemukan',
        'isi': 'Maaf halaman ini tidak tersedia. Silakan cek kembali URL yang anda tuju.'
    }
    return render(request, '404.html', context)
