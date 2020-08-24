from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm


def cart_add(request, product_id):
    """Adding product into cart."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    else:
        cart.add(product=product,
                quantity= 1,
                update_quantity= False)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    """Removing product from cart."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    """Reflecting content of cart."""
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'coupon_apply_form':coupon_apply_form})