from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemAdmin(admin.TabularInline):
    model = MenuItem
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemAdmin]

admin.site.register(Menu, MenuAdmin)

