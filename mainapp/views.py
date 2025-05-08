from django.shortcuts import render

from mainapp.models import Product

def index(request):
    title = 'Главная страница'

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
    title = ''

    context = {
        'title': title,
    }
    return render(request, 'products.html', context)



def product(request):
    title = ''

    context = {
        'title': title,
    }
    return render(request, 'product.html', context)
