from app.views import *
from app.services.language_service import *
from core.settings import BASE_DIR
import os
from app.models import *
from django.shortcuts import get_object_or_404

def pages(request, page='index'):
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    products = Product.objects.all()
    context = {
        'page': page, 'products': products, 'categories': categories, 'sub_categories': sub_categories, 
        }
    return render(request, f'pages/{page}.html', context)

def category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    context = {'categories': categories, 'obj': category}
    return render(request, 'pages/category.html', context)

def sub_category(request, pk):
    categories = Category.objects.all()
    sub_category = get_object_or_404(SubCategory, pk=pk)
    context = {'categories': categories, 'obj': sub_category}
    return render(request, 'pages/sub_category.html', context)


def change_lang(request, lang):
    ip = get_user_ip(request)
    update_lang_by_ip(ip, int(lang))
    return redirect_back(request)


def get_file(request, path):
    file = open(os.path.join(BASE_DIR, f'files/{path}'), 'rb')
    return FileResponse(file)