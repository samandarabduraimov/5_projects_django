from django.shortcuts import render
from .models import Category, Pets
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_pets(request, pk):
    pets =Pets.objects.filter(category=pk)
    context = {
        'pets': pets
    }
    return render(request, 'pets.html', context=context)

def detail(request, pk):
    pets = Pets.objects.get(pk=pk)
    context = {
        'pets': pets
    }
    print(1)
    return render(request, 'detail.html', context=context)