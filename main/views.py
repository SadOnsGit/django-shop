from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def testpage(request):
    return render(request, 'mytestapp/index.html')

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина',
        'list': [4, 'second']
    }
    
    return render(request, 'mytestapp/index.html', context=context)
