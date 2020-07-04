from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from shop import paginator_helper


def index(request):
    products = Product.objects.all().order_by('-created')[:6]
    return render(request, 'index.html', {'products': products})

def product_list(request, category_slug=None):
    """Отображение товаров каталога."""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = paginator_helper.pg_records(request, products, 9)
    context[category] = category
    context[categories] = categories
    return render(request, 'product/list.html', context)

def product_detail(request, id, slug):
    """Отображение описания товара."""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'product': product,  'cart_product_form': cart_product_form})

def delivery(request):
    return render(request, 'delivery_payment/delivery.html')

def payment(request):
    return render(request, 'delivery_payment/payment.html')

def returning(request):
    return render(request, 'delivery_payment/returning.html')

def about(request):
    return render(request, 'about.html')