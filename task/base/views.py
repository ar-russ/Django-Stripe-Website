from django.shortcuts import render, redirect
from .models import Item, Order
from . import payment_services


def home_page(request):
    return redirect('items')


def items_page(request):
    items = Item.objects.all()
    order = Order.objects.get(id=1) # In future can be replaced as request.user.order
    items_in_order = order.get_items_in_order()
    context = {
        'items': items,
        'order': order,
        'items_in_order': items_in_order
    }
    return render(request, 'base/items.html', context)


def item_page(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'base/item.html', context)


def buy_page(request, pk):
    item = Item.objects.get(id=pk)
    session = payment_services.create_checkout_session(
        name=item.name, 
        price=item.price
    )
    return redirect(session.url)


def buy_ordered(request):
    order = Order.objects.get(id=1) # In future can be replaced as request.user.order
    if len(order.get_as_list()) < 1:
        return redirect('items')
    order_name = ', '.join([
        item.name for item in order.get_items_in_order()
    ])
    session = payment_services.create_checkout_session(
        name=order_name, 
        price=order.total_cost
    )
    return redirect(session.url)


def add_item_to_order(request, pk):
    item = Item.objects.get(id=pk)
    order = Order.objects.get(id=1) # In future can be replaced as request.user.order
    order.add_item(item)
    return redirect('items')
    

def delete_item_from_order(request, pk):
    item = Item.objects.get(id=pk)
    order = Order.objects.get(id=1) # In future can be replaced as request.user.order
    order.delete_item(item)
    return redirect('items') 


def clear_order(request):
    order = Order.objects.get(id=1) # In future can be replaced as request.user.order
    order.clear()
    return redirect('items')


def success_page(request):
    return render(request, 'base/success.html')


def cancel_page(request):
    return render(request, 'base/cancel.html')
