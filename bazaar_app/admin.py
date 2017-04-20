from django.contrib import admin

from .models import BazaarBook

class BazaarBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'id', 'price')

admin.site.register(BazaarBook, BazaarBookAdmin)
