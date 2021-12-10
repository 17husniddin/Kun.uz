from django.contrib import admin

from .models import Homepage

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    list_display_links = ('name',)
    search_fields = ('name', 'image')
# Register your models here.

admin.site.register(Homepage)