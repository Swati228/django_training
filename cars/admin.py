from django.contrib import admin
from .models import Car
from django.utils.html import format_html #to use html inside pyhton
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border_radius:50px" />'.format(object.car_photo.url))

    thumbnail.short_description = 'car_photo'

    list_display =('id','thumbnail','car_title','state','color','model','fuel_type','is_featured')
    list_display_links =('id','thumbnail','car_title')
    search_fields =('id','car_title','model','fuel_type')
    list_filter =('model','fuel_type')
    list_editable =('is_featured',) #to make row editable



admin.site.register(Car , CarAdmin )
