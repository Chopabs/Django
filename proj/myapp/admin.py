from django.contrib import admin

from .models import Room, topic, message

#Set List
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'topic', 'updated', 'created')
    search_fields = ('name', 'description')
    list_filter = ('topic', 'host')

admin.site.register(Room, RoomAdmin)
admin.site.register(topic)
admin.site.register(message) 
