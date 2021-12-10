from django.contrib import admin


from .models import *

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'images')
    list_display_links = ('name',)
    search_fields = ('name', 'images')
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(News)
# Register your models here.
