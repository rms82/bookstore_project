from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm, CommentForm


# Create your views here.
class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        return Book.objects.select_related('created_by')


@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': comments,
        'comment_form': comment_form
    })


class BookCreateView(LoginRequiredMixin,generic.CreateView):
    form_class = BookForm
    template_name = 'books/book_new.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    
class BookUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    form_class = BookForm
    queryset = Book.objects.all()
    template_name = 'books/book_update.html'

    def test_func(self):
        return self.get_object().created_by == self.request.user
