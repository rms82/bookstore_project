from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),

    path('new_book/', views.BookCreateView.as_view(), name='new_book')
]