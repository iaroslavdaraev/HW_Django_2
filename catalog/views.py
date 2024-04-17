from django.shortcuts import render

from catalog.models import Product


def index_homepage(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/homepage.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, id):
    product_object = Product.objects.get(pk=id)
    context = {
        'object': product_object,
        'title': product_object.name
    }
    return render(request, 'catalog/product.html', context)
