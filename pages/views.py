from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages

from .forms import BookForm,Categoryform
# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BookForm, Categoryform
from .models import Book, Category

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'Congratulations! The job has been successfully posted. We look forward to receiving qualified candidates!')  # Only call this once
            return redirect('/')

    # Fetch data for the template
    category = Category.objects.all()
    book = Book.objects.all()
    
    # Prepare context for the template
    context = {
        'book': book,
        'category': category,
        'form': BookForm(),
        'categor': Categoryform(),
    }

    return render(request, 'pages/index.html', context)

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