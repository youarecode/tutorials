from django.contrib import admin
from .models import Category, Post
# Register your models here.


class Category_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class Post_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Category, Category_admin)
admin.site.register(Post, Post_admin)