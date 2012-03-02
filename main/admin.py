from django.contrib import admin
from main.models import Zombie, Twit


class ZombieAdmin(admin.ModelAdmin):
    list_display = ('name', 'cemetery',)
    search_fields = ('name',)


class TwitAdmin(admin.ModelAdmin):
    list_display = ('zombie', 'status', 'created_at',)


admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Twit, TwitAdmin)
