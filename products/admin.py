from django.contrib import admin
from .models import Author, Category, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'created_time', 'is_enable', ]
    list_display_links = ['id', 'name']
    readonly_fields = ['created_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'is_enable']
    # list_display_links = [id]
    search_fields = ['title']


# class CategoryInline(admin.TabularInline):
#     model = Category
#     fields = ['title', 'parent']
#     extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'author', 'category', 'is_enable', 'file', ]
    list_display = ['id', 'name', 'created_time', 'is_enable', ]
    search_fields = ['name', ]
    filter_horizontal = ['author', 'category']
# filter_vertical = ['category']
# inlines = [CategoryInline]
