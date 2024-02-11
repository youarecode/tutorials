from django.contrib import admin
from webapp.models import Clients, Article, Orders

# Register your models here.

class Clients_admin(admin.ModelAdmin):
    """This class allows you to show more information in the admin page"""
    list_display = ("name","address","phone")
    search_fields = ("name", "phone")


class Articles_admin(admin.ModelAdmin):
    list_filter = ('category',)

class Orders_admin(admin.ModelAdmin):
    list_display = ('number','date')
    list_filter = ('date',)
    date_hierarchy = 'date'

admin.site.register(Clients, Clients_admin)
admin.site.register(Article, Articles_admin)
admin.site.register(Orders, Orders_admin)