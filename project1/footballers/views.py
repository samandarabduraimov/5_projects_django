from django.shortcuts import render
from .models import Category, Footballers
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_footballers(request, pk):
    footballers = Footballers.objects.filter(category=pk)
    context = {
        'footballers': footballers
    }
    return render(request, 'footballers.html', context=context)

def detail(request, pk):
    footballers = Footballers.objects.get(pk=pk)
    context = {
        'footballers': footballers
    }
    print(1)
    return render(request, 'detail.html', context=context)