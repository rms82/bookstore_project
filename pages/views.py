from django.shortcuts import redirect


# Create your views here.
def home_page(request):
    return redirect('book_list')

