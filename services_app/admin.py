from django.contrib import admin
from . import models

# Register your models here.

class Services_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(models.Service, Services_admin)