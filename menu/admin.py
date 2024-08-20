from django.contrib import admin
from .models import MenuItem, Menu



@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'url']
    prepopulated_fields = {'url': ('name',)}