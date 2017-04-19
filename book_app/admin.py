from django.contrib import admin

from .models import Author, Book, Rate

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')

class RateAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Rate, RateAdmin)
