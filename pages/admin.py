from django.contrib import admin
from .models import Category, Book

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Fields to display in the admin list view
    search_fields = ('name',)  # Add a search bar for the 'name' field


# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'price', 'rental_price_day', 'status', 'active')  # Display key fields
    list_filter = ('status', 'category', 'active')  # Add filters for these fields
    search_fields = ('title', 'author')  # Add a search bar for 'title' and 'author'
    list_editable = ('status', 'active')  # Make 'status' and 'active' editable in the list view
    fieldsets = (  # Organize fields in the detail view
        ('Basic Info', {
            'fields': ('title', 'author', 'category', 'status', 'active')
        }),
        ('Additional Info', {
            'fields': ('photo_book', 'photo_author', 'pages', 'price', 'rental_price_day', 'rental_period')
        }),
    )
