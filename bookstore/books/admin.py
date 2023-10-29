# admin/admin.py

from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    # max_num = 2  # Defines no of rows


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )


admin.site.register(Book, BookAdmin)
