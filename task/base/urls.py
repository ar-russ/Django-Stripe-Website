from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('items', views.items_page, name='items'),
    path('buy/<pk>', views.buy_page, name='buy'),
    path('add-item-to-order/<pk>', views.add_item_to_order, name='add-item-to-order'),
    path('delete-item-from-order/<pk>', views.delete_item_from_order, name='delete-item-from-order'),
    path('clear-order', views.clear_order, name='clear-order'),
    path('buy-ordered', views.buy_ordered, name='buy-ordered'),
    path('item/<pk>', views.item_page, name='item'),
    path('success', views.success_page, name='success'),
    path('cancel', views.cancel_page, name='cancel'),
]
