from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        'title': 'О нас',
        'content': 'Страница о нас',
        'page_text': 'Мы работаем с 2008 года'
    }
    return render(request, 'mytestapp/about.html', context=context)

def index(request):
    context = {
        'title': 'Главная',
        'content': 'Главная страница магазина'
    }
    
    return render(request, 'mytestapp/index.html', context=context)