from django.urls import path

from task4.views import main_page, basket_page, shop_page

urlpatterns = [
path('main_page/', main_page),
    path('basket_page/', basket_page),
    path('shop_page/', shop_page),
]