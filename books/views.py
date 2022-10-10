from django.shortcuts import render
from django.views import generic

from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    model = Book


class BookCreateView(generic.CreateView):
    form_class = BookForm
    template_name = 'books/book_new.html'
