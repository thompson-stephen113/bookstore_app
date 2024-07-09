from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book

# Create your views here.
# CBV "BookListView", protected
class BookListView(LoginRequiredMixin, ListView):
    model = Book

    template_name = "books/main.html"

# CBV "BookDetailView", protected
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

    template_name = "books/detail.html"
