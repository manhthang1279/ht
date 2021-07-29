from django.contrib import admin
from .models import Category, Book, BookLendDetail


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Book information', {'fields': [
            'isbn',
            'author',
            'company',
            'year_publish',
            'price',
            'category',
            'sub_category',
            'status'
        ]}),
    ]
    list_display = ('title', 'isbn', 'status')
    list_filter = ['status']
    search_fields = ['title']


# admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(BookLendDetail)
