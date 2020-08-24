from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .models import Category, Product
from cart.forms import CartAddProductForm
from . forms import ContactForm
from shop import paginator_helper



def index(request):
    """Main page."""
    products = Product.objects.filter(available=True).order_by('-created')[:6]
    return render(request, 'index.html', {'products': products})

def product_list(request, category_slug=None):
    """Displaying list of products."""
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = paginator_helper.pg_records(request, products, 9)
    context['category'] = category
    context['categories'] = categories
    return render(request, 'product/list.html', context)

def product_detail(request, id, slug):
    """Displaying products description."""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'product': product,  'cart_product_form': cart_product_form})

def search(request):
    """Reflecting search results"""
    query = request.GET.get("keyword").strip()
    if query:
        products = Product.objects.filter(name__icontains= query)
        context = paginator_helper.pg_records(request, products, 9)
        context['query_parameter'] = f'&keyword={query}'
        context['query'] = query
        print(context)
        return render(request, 'product/search.html', context)
    else:
        return render(request, 'product/search.html', {'query': query})

def contacts(request):
    """Contacts form for sending email."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['WASILIY10K@yandex.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'vasiliy.kavaleu@gmail.com', recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'index.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def delivery(request):
    return render(request, 'delivery_payment/delivery.html')

def payment(request):
    return render(request, 'delivery_payment/payment.html')

def about_us(request):
    return render(request, 'about.html')


