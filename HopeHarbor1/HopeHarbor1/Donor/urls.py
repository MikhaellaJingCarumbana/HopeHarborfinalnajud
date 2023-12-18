from django.urls import path
from . import views

app_name = 'donor'

urlpatterns = [
    path('', views.donor_entry_request, name='login'),
    path('register/', views.registration, name='register'),

    path('CashPage', views.Cash.as_view(), name='CashPage'),
    path('Cash', views.InsertCashDonation.as_view(), name='Cash'),
    path('CashTracker', views.displayAmountTracker.as_view(), name='CashTracker'),

    path('DiK', views.DiK.as_view(), name='DiK'),
    path('goods', views.InsertGoods.as_view(), name='goods'),
    path('goodstracker', views.displayGoodsTracker.as_view(), name='goodstracker')
]
