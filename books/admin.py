from django.contrib import admin
from .models import Genre, Author, Book, Favorite, Review

# admin.site.register(Genre)
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(Favorite)
# admin.site.register(Review)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date')
    search_fields = ('title', 'author__name')
    list_filter = ('genre', 'author', 'publication_date')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)