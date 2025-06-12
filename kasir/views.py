from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Transaksi, ItemTransaksi

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
    items = ItemTransaksi.objects.filter(transaksi=transaksi)

    item_list = []
    total = 0
    for item in items:
        subtotal = item.menu.harga * item.jumlah
        total += subtotal
        item_list.append({
            'menu': item.menu,
            'jumlah': item.jumlah,
            'harga_format': format_rupiah(item.menu.harga),
            'subtotal_format': format_rupiah(subtotal)
        })

    return render(request, 'kasir/nota.html', {
        'transaksi': transaksi,
        'items': item_list,
        'total': format_rupiah(total)
    })
def format_rupiah(angka):
    return "Rp {:,}".format(int(angka)).replace(",", ".")