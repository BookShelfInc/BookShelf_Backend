from django.contrib import admin

from .models import Wishlist, Quote, Bookshelf

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('user',)

class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Bookshelf, BookshelfAdmin)
