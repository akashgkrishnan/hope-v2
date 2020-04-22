from django.forms import ModelForm
from . models import book_inventory


class BookForm(ModelForm):
    class Meta:
        model = book_inventory
        fields = [
            'book_name',
            'book_author',
            'genre',
            'number_of_books',
            'book_number'
        ]