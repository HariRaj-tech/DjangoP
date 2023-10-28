# books/view.py

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"
    login_url = "account_login"


class BookDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView,
):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    # queryset = Book.objects.filter(title__icontains="api")

    def get_queryset(self):
        user_ip = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if user_ip:
            ip = user_ip.split(",")[0]
        else:
            ip = self.request.META.get("REMOTE_ADDR")

        print("Request from : ", ip)
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
