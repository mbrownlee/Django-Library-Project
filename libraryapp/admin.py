from django.contrib import admin
from libraryapp.models import Book

class BookAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Book, BookAdmin)