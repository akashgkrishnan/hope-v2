from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
# models
from .models import book_inventory
# forms
from .forms import BookForm



# Create your views here.
def library_index(request):
    book = book_inventory.objects.all()
    print(book)
    sum_all_books = sum((item.number_of_books for item in book))
    form = BookForm()
    return render(request, 'librarian/base.html', {'sum_all_books': sum_all_books,
                                                   'books': book,
                                                   'form': form})

@require_POST
def add_books(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        book_name = form.cleaned_data.get('book_name')
        messages.success(request, f'{book_name} added to the library book inventory')
        return redirect('librarian-home')
    messages.warning(request, 'some error occured while saving try again')
    redirect('librarian-home')








        # form = BookForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     bsr = form.cleaned_data.get('book_name')
        #     messages.success(request, f' {bsr} Added to inventory!')
        #     return redirect('library-inventory')
        # messages.warning(request, 'there was some problem in saving last request please try again!')
        # return redirect('librarian-home')
