from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, null=True)
    full_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    book_status = (
        ('Trong kho', 'Trong kho'),
        ('Đang mượn', 'Đang mượn')
    )
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    company = models.CharField(max_length=500)
    price = models.IntegerField()
    year_publish = models.IntegerField()
    sub_category = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=book_status, blank=True, default='Trong kho')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class BookLendDetail(models.Model):
    book_status = (
        ('Trong kho', 'Trong kho'),
        ('Đang mượn', 'Đang mượn')
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    reader = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    lent_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    charge = models.IntegerField()
    status = models.CharField(max_length=20, choices=book_status, blank=True, default='Trong kho')

    def __str__(self):
        return self.book.title

    @property
    def is_overdue(self):
        if self.return_date and date.today() > self.return_date:
            return True
        return False
