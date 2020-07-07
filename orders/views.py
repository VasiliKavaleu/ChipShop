from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    """Reflecting orders form."""
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # getting coupon and discount from sessions before saving
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
                cart.clear()
                return render(request,
                            'orders/order/created.html',
                            {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                'orders/order/create.html',
                {'cart': cart, 'form': form})
