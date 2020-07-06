from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search', views.search, name='search_results'),
    path('delivery', views.delivery, name='delivery'),
    path('payment', views.payment, name='payment'),
    path('aboutus', views.about_us, name='about_us'),
]