from django.urls import path
from . import views

urlpatterns = [
    path('pesan/', views.buat_pesanan, name='buat_pesanan'),
    path('nota/<int:transaksi_id>/',views.nota, name='nota'),
]