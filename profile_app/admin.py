from django.contrib import admin

from .models import Wishlist, Quote, Bookshelf

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'has_read', 'id')

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')

class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'id')

admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Bookshelf, BookshelfAdmin)
