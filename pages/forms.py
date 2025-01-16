from django import forms
from .models import Category,Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        