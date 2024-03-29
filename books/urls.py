from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.book_detail_view, name='book_detail'),
    path('<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),

    path('new_book/', views.BookCreateView.as_view(), name='new_book')
]
