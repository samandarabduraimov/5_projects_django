from django.shortcuts import render
from .models import Category, Phones
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_phones(request, pk):
    phones =Phones.objects.filter(category=pk)
    context = {
        'phones': phones
    }
    return render(request, 'phones.html', context=context)

def detail(request, pk):
    phones = Phones.objects.get(pk=pk)
    context = {
        'phones': phones
    }
    print(1)
    return render(request, 'detail.html', context=context)