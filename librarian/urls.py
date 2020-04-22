from django.urls import path
from . import views


urlpatterns = [
    path('librarian-home', views.library_index, name='librarian-home'),
    path('add-library-books', views.add_books, name='add-library-books')
]