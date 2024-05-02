from django.shortcuts import render
from .models import Category, Towers
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_towers(request, pk):
    towers =Towers.objects.filter(category=pk)
    context = {
        'towers': towers
    }
    return render(request, 'towers.html', context=context)

def detail(request, pk):
    towers = Towers.objects.get(pk=pk)
    context = {
        'towers': towers
    }
    print(1)
    return render(request, 'detail.html', context=context)