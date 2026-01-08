from django.urls import path
from transfer_money import views

urlpatterns = [
    path('transfer-money/', views.transfer_money, name='transfer'),
    path('', views.home, name='home'),
]
