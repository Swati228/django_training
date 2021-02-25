from django.contrib import admin
from .models import Team
from django.utils.html import format_html #to use html inside pyhton

class TeamAdmin(admin.ModelAdmin):
     def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border_radius:100px" />'.format(object.photo.url))

     thumbnail.short_description = 'photo'


      #thses variable are inbuilt pass thumbail for photo
     list_display = ("id","thumbnail","first_name","designation","created_date") #show thses in thead inside Teams admin
     list_display_links = ('id','thumbnail','first_name') #to make the link clickable
     search_fields = ('first_name','last_name','designation') #to add search bar inside admin panel
     list_filter = ('designation',) #to make more then elemnts filters

# Register your models here.
admin.site.register(Team , TeamAdmin)
