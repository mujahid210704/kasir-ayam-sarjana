from django.db import models

class Menu(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.IntegerField()

    def __str__(self):
        return self.nama

class Transaksi(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)

    @property
    def total_bayar(self):
        return sum(item.total_harga for item in self.itemtransaksi_set.all())

class ItemTransaksi(models.Model):
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    jumlah = models.IntegerField()

    @property
    def total_harga(self):
        return self.menu.harga * self.jumlah
