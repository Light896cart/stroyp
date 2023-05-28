from django.contrib import admin
from .models import *




class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name','phoneNumber',
                    'paid',
                    'created', 'updated']

    list_filter = ['paid', 'created', 'updated']

class WorkAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','photo']
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ['id','name']
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Order, OrderAdmin)
admin.site.register(Work, WorkAdmin)
