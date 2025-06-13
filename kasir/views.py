from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Menu, Transaksi, ItemTransaksi

def index(request):
    return HttpResponse("<h1>Selamat Datang di Aplikasi Kasir Ayam Sarjana!</h1>")

def buat_pesanan(request):
    menu_list = Menu.objects.all()

    if request.method == "POST":
        transaksi = Transaksi.objects.create()
        for menu in menu_list:
            jumlah = int(request.POST.get(f'menu_{menu.id}', 0))
            if jumlah > 0:
                ItemTransaksi.objects.create(
                    transaksi=transaksi,
                    menu=menu,
                    jumlah=jumlah
                )
        return redirect('nota', transaksi_id=transaksi.id)

    return render(request, 'kasir/form_pesanan.html', {'menu_list': menu_list})

def nota(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, id=transaksi_id)
    return render(request, 'kasir/nota.html', {'transaksi': transaksi})
