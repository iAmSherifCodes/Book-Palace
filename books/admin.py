from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
# from .models import User


# from .models import User


# Register your models here.

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "first_name", "last_name", "email"),
            },
        ),
    )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'isbn', 'author']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['genre']


# add BookAdmin into admin.site.register
# admin.site.register(models.Book, BookAdmin)

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_filter = ['first_name', 'last_name']
    search_fields = ['email']

# admin.site.register(models.Author, AuthorAdmin)
