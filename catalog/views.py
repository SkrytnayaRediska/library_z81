# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from catalog.models import Genre, Language, \
    Book, BookInstance, Author
from django.views.generic import ListView, DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='Available').count()

    return render(request, 'index.html', {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available
    })


class AuthorsListView(ListView):
    model = Author
    template_name = 'authors_list.html'
    context_object_name = 'authors_list'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class BooksListView(ListView):
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books_list'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookInstanceDetailView(DetailView):
    model = BookInstance
    context_object_name = 'book_instance'
    template_name = 'book_instance_detail.html'
