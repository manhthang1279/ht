from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book
from .filters import BookFilter


# Create your views here.
def index(request):
    table_filter = BookFilter(request.GET, queryset=Book.objects.all())

    paginator = Paginator(table_filter.qs, 50)
    page_number = request.GET.get('page')
    context = paginator.get_page(page_number)

    return render(request, 'library/index.html', {
        'context': context,
        'table_filter': table_filter
    })

# def index(request):
#     if request.method == 'POST':
#         table_filter = request.POST.getlist('table_filter')
#     else:
#         table_filter = BookFilter(request.GET, queryset=Book.objects.all())
#
#     paginator = Paginator(table_filter.qs, 50)
#     page_number = request.GET.get('page')
#     context = paginator.get_page(page_number)
#
#     return render(request, 'library/index.html', {
#         'context': context,
#         'table_filter': table_filter
#     })
