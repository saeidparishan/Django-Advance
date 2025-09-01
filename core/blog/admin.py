from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "status", "published_date", "category"]
    search_fields = ("title",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
