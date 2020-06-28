from django.utils.deprecation import MiddlewareMixin
from shop.models import Category

class GetCategory(MiddlewareMixin):
    def process_request(self, request):
        category_list= Category.objects.all()
        request.category_list = category_list
        return None