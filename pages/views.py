from django.shortcuts import redirect,get_object_or_404, render
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
            messages.success(request, 'Congratulations! you add Book')  # Only call this once
            return redirect('/')
        
        
        # category
        form1 = Categoryform(request.POST, request.FILES)
        if form1.is_valid():
            myform1 = form1.save(commit=False)
            myform1.owner = request.user
            myform1.save()
            messages.success(request, 'Congratulations You Added Category!')  # Only call this once
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


def update(request, id):
    book_id = get_object_or_404(Book, id=id)
    
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            messages.success(request, 'Congratulations! The book has been updated successfully.')  # Add success message
            return redirect('/')  # Redirect to a detail view

            # Optionally, you can add a redirect here after successful save
            # from django.shortcuts import redirect
            # return redirect('some_view_name')
    else:
        book_save = BookForm(instance=book_id)
    
    context = {
        'form4': book_save,
    }
    return render(request, 'pages/update.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    
    if request.method == 'POST':
        # Check if the form was submitted with the delete action
        if 'delete' in request.POST:
            book.delete()
            messages.success(request, 'Congratulations! The book has been deleted successfully.')
            return redirect('/')
        # Check if the form was submitted with the cancel action
        elif 'cancel' in request.POST:
            return redirect('/')  # Redirect without deleting the book
    
    return render(request, 'pages/delete.html', {'book': book})