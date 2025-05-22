from django.shortcuts import render

from mainapp.models import Product, Category

def index(request):
    title = 'Главная'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods,
    }
    return render(request, 'index.html', context)



def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)



def about(request):
    title = 'O нас'
    context = {
        'title': title,
    }
    return render(request, 'about.html', context)



def products(request):
    title = 'Товары'
    prods = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
    }
    return render(request, 'products.html', context)



def product(request):
    title = 'Товар'

    prod = Product.objects.get(id=1)
    same_prods = Product.objects.exclude(id=prod.id)

    context = {
        'title': title,
        'product': prod,
        'products': same_prods,
    }
    return render(request, 'product.html', context)
