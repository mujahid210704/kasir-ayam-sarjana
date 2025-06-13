from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pesan/', views.buat_pesanan, name='buat_pesanan'),
    path('nota/<int:transaksi_id>/', views.nota, name='nota'),
]
