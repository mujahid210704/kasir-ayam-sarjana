from django.contrib import admin
from .models import Menu, Transaksi, ItemTransaksi

# Registrasi model biar muncul di admin Django
admin.site.register(Menu)
admin.site.register(Transaksi)
admin.site.register(ItemTransaksi)