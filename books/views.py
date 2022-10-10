from django.shortcuts import render
from django.views import generic

from .models import Book


# Create your views here.
class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'books'
