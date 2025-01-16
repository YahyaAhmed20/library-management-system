from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    category=Category.objects.all()
    book=Book.objects.all()
    context={'book':book,'category':category}


    return render(request, 'pages/index.html',context)

def books(request):
    category=Category.objects.all()
    book=Book.objects.all()
    context={'book':book,'category':category}

    return render(request, 'pages/books.html',context)


def update(request):
    category=Category.objects.all()
    book=Book.objects.all()
    context={'book':book,'category':category}
    return render(request, 'pages/update.html',context)

def delete(request):
    category=Category.objects.all()
    book=Book.objects.all()
    context={'book':book,'category':category}
    return render(request, 'pages/delete.html',context)