from django.shortcuts import render

def catalog(request):
    context = {
        'title': 'Товары',
        'data': [
            {
                'name': 'Товар №1',
                'price': 1000
            },
            {
                'name': 'Товар №2',
                'price': 1000
            },
            {
                'name': 'Товар №3',
                'price': 1000
            },
            {
                'name': 'Товар №4',
                'price': 1000
            },
            {
                'name': 'Товар №5',
                'price': 1000
            },
        ]
    }
    return render(request, 'catalog/catalog.html', context=context)

def product(request):
    return render(request, 'catalog/product.html')