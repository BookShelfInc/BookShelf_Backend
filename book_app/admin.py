from django.contrib import admin

from .models import Author, Book, Rate, Review

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'id')

class RateAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'id', 'rating')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'id')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Review, ReviewAdmin)
