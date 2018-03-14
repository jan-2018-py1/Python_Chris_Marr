from __future__ import unicode_literals
from .models import Quote, Author, Book
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'recent': Quote.objects.recent_and_not()[0],
        'more': Quote.objects.recent_and_not()[1]
    }
    return render(request, 'second_app/index.html', context)

def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'second_app/add.html', context)

def show(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'second_app/show.html', context)

def create(request):
    errs = Quote.objects.validate_quote(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        book_id = Quote.objects.create_quote(request.POST, request.session['user_id']).book.id
    return redirect('/books/{}'.format(book_id))

def create_additional(request, book_id):
    the_book = Book.objects.get(id=book_id)
    new_book_data = {
        'title': the_book.title,
        'author': the_book.author.id,
        'rating': request.POST['rating'],
        'quote': request.POST['quote'],
        'new_author': ''
    }
    errs = Quote.objects.validate_quote(new_book_data)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        Quote.objects.create_quote(new_book_data, request.session['user_id'])
    return redirect('/books/' + book_id)